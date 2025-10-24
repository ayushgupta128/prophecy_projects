{% macro generate_html_table_from_relation(
		relation,
		columns=None,
		where_clause=None,
		order_by=None,
		limit=100,
		caption=None,
		table_class='dbt-table',
		include_index=True,
		column_formats=None,
		add_col_classes=True,
		summary=None
) -%}
{%- set rel_sql = relation|string -%}
{%- if columns is sequence and columns|length > 0 -%}
	{%- set cols_sql = (columns | map('string') | list) | join(', ') -%}
{%- else -%}
	{%- set cols_sql = '*' -%}
{%- endif -%}

{%- set parts = [] -%}
{%- do parts.append('select ' ~ cols_sql ~ ' from ' ~ rel_sql) -%}
{%- if where_clause -%}
	{%- do parts.append(' where ' ~ where_clause) -%}
{%- endif -%}
{%- if order_by -%}
	{%- do parts.append(' order by ' ~ order_by) -%}
{%- endif -%}
{%- if limit is number and limit > 0 -%}
	{%- do parts.append(' limit ' ~ limit) -%}
{%- endif -%}

{%- set sql = parts | join('') -%}

{{ return(
	generate_html_table(
		sql=sql,
		caption=caption,
		max_rows=limit,
		table_class=table_class,
		include_index=include_index,
		column_formats=column_formats,
		infer_formats=false,
		defaults=None,
		add_col_classes=add_col_classes,
		summary=summary
	)
) }}

{%- endmacro %}