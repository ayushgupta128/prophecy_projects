{% macro concat_html_tables(sections) -%}

{%- set out = [] -%}
{%- for s in sections -%}
	{%- if s.title is defined and s.title -%}
		{%- do out.append('<h2>' ~ s.title|e ~ '</h2>') -%}
	{%- endif -%}
	{%- if s.html is defined and s.html -%}
		{%- do out.append(s.html) -%}
	{%- endif -%}
	{%- if not loop.last -%}
		{%- do out.append('<hr/>') -%}
	{%- endif -%}
{%- endfor -%}

{{ return(out|join('\n')) }}
{%- endmacro %}