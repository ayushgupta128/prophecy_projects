{% macro generate_html_table(sql, caption=None, max_rows=100, table_class='', include_index=False, column_formats=None, infer_formats=False, defaults=None, add_col_classes=True, summary=None) -%}

{%- set result = run_query(sql) -%}
{%- if not result -%}
	{{ return('') }}
{%- endif -%}

{%- set columns = [] -%}
{%- for col in result.columns -%}
	{%- do columns.append( (col.name | default(col.column)) ) -%}
{%- endfor -%}

{%- set rows = result.rows -%}
{%- set defaults = defaults or {} -%}
{%- set fmts = {} -%}
{%- if column_formats is mapping -%}
	{%- do fmts.update(column_formats) -%}
{%- endif -%}

{%- if infer_formats and rows and rows|length > 0 -%}
	{%- set first = rows[0] -%}
	{%- for c in range(0, columns|length) -%}
		{%- set col_name = columns[c] -%}
		{%- if fmts.get(col_name) is not defined -%}
			{%- set inferred = infer_format_for_value(first[c], defaults) -%}
			{%- do fmts.update({ (col_name): inferred }) -%}
		{%- endif -%}
	{%- endfor -%}
{%- endif -%}

{# Derive column type for classes based on provided formats #}
{%- set col_kinds = {} -%}
{%- for c in range(0, columns|length) -%}
	{%- set col_name = columns[c] -%}
	{%- set fmt = fmts.get(col_name) -%}
	{%- if fmt is mapping -%}
		{%- set kind = fmt.get('type', 'text') -%}
	{%- elif fmt is string -%}
		{%- set kind = fmt -%}
	{%- else -%}
		{%- set kind = 'text' -%}
	{%- endif -%}
	{%- do col_kinds.update({ (col_name): kind }) -%}
{%- endfor -%}

{%- set html = [] -%}
{%- do html.append('<table' ~ (' class="' ~ table_class ~ '"' if table_class else '') ~ '>') -%}

{%- if caption -%}
	{%- do html.append('<caption>' ~ caption|e ~ '</caption>') -%}
{%- endif -%}

{%- do html.append('<thead><tr>') -%}
{%- if include_index -%}
	{%- do html.append('<th class="col-index">#</th>') -%}
{%- endif -%}
{%- for c in columns -%}
	{%- set th_cls = '' -%}
	{%- if add_col_classes -%}
		{%- set kind = col_kinds.get(c, 'text') -%}
		{%- set th_cls = ' class="col-' ~ kind ~ '"' -%}
	{%- endif -%}
	{%- do html.append('<th' ~ th_cls ~ '>' ~ c|e ~ '</th>') -%}
{%- endfor -%}
{%- do html.append('</tr></thead>') -%}

{%- do html.append('<tbody>') -%}
{%- for row in rows[:max_rows] -%}
	{%- do html.append('<tr>') -%}
	{%- if include_index -%}
		{%- do html.append('<td class="col-index">' ~ loop.index ~ '</td>') -%}
	{%- endif -%}
	{%- for ci in range(0, columns|length) -%}
		{%- set cell = row[ci] -%}
		{%- set col_name = columns[ci] -%}
		{%- set fmt = fmts.get(col_name) -%}
		{%- if fmt is defined and fmt is not none -%}
			{%- set rendered = format_cell(cell, fmt) -%}
		{%- else -%}
			{%- set rendered = (cell if cell is not none else '') -%}
		{%- endif -%}
		{%- set td_cls = '' -%}
		{%- if add_col_classes -%}
			{%- set kind = col_kinds.get(col_name, 'text') -%}
			{%- set td_cls = ' class="col-' ~ kind ~ '"' -%}
		{%- endif -%}
		{%- do html.append('<td' ~ td_cls ~ '>' ~ (rendered|string)|e ~ '</td>') -%}
	{%- endfor -%}
	{%- do html.append('</tr>') -%}
{%- endfor -%}
{%- do html.append('</tbody>') -%}

{%- if summary is mapping and rows and rows|length > 0 -%}
	{%- set sums = {} -%}
	{%- set counts = {} -%}
	{%- for row in rows[:max_rows] -%}
		{%- for ci in range(0, columns|length) -%}
			{%- set col_name = columns[ci] -%}
			{%- set agg = summary.get(col_name) -%}
			{%- if agg in ['sum','avg','count'] -%}
				{%- set val = row[ci] -%}
				{%- if agg == 'count' -%}
					{%- set _ = counts.update({ (col_name): (counts.get(col_name, 0) + 1) }) -%}
				{%- elif val is number -%}
					{%- set _ = sums.update({ (col_name): (sums.get(col_name, 0) + val) }) -%}
					{%- set _ = counts.update({ (col_name): (counts.get(col_name, 0) + 1) }) -%}
				{%- endif -%}
			{%- endif -%}
		{%- endfor -%}
	{%- endfor -%}

	{%- do html.append('<tfoot><tr>') -%}
	{%- if include_index -%}
		{%- do html.append('<td class="col-index"></td>') -%}
	{%- endif -%}
	{%- for c in columns -%}
		{%- set agg = summary.get(c) -%}
		{%- if agg == 'sum' -%}
			{%- set val = sums.get(c) -%}
		{%- elif agg == 'avg' -%}
			{%- set cnt = counts.get(c, 0) -%}
			{%- set val = (sums.get(c) / cnt) if cnt > 0 else none -%}
		{%- elif agg == 'count' -%}
			{%- set val = counts.get(c) -%}
		{%- else -%}
			{%- set val = none -%}
		{%- endif -%}
		{%- set fmt = fmts.get(c) -%}
		{%- set rendered = (format_cell(val, fmt) if (fmt is defined and val is not none) else (val if val is not none else '')) -%}
		{%- set td_cls = '' -%}
		{%- if add_col_classes -%}
			{%- set kind = col_kinds.get(c, 'text') -%}
			{%- set td_cls = ' class="col-' ~ kind ~ ' summary"' -%}
		{%- endif -%}
		{%- do html.append('<td' ~ td_cls ~ '>' ~ (rendered|string)|e ~ '</td>') -%}
	{%- endfor -%}
	{%- do html.append('</tr></tfoot>') -%}
{%- endif -%}

{%- do html.append('</table>') -%}

{{ return(html|join('')) }}

{%- endmacro %}





