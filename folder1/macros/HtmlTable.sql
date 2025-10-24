{% macro HtmlTable(sections) -%}
{%- set built = [] -%}
{%- for s in sections -%}
	{%- set title = s.get('title') -%}
	{%- set relation = s.get('relation') -%}
	{%- if not relation -%}
		{%- continue -%}
	{%- endif -%}
	{%- set html = generate_html_table_from_relation(
			relation=relation,
			columns=s.get('columns'),
			where_clause=s.get('where_clause'),
			order_by=s.get('order_by'),
			limit=(s.get('limit') or 100),
			caption=s.get('caption'),
			table_class=(s.get('table_class') or 'dbt-table'),
			include_index=(s.get('include_index') if s.get('include_index') is not none else true),
			column_formats=s.get('column_formats'),
			add_col_classes=(s.get('add_col_classes') if s.get('add_col_classes') is not none else true),
			summary=s.get('summary')
	) -%}
	{%- do built.append({'title': title, 'html': html}) -%}
{%- endfor -%}

{{ return("Select '" ~ concat_html_tables(built)|replace("'", "''") ~ "' AS out_column") }}

{%- endmacro %}

