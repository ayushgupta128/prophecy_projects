
from dataclasses import dataclass

from typing import List
from collections import defaultdict
from prophecy.cb.sql.Component import *
from prophecy.cb.sql.MacroBuilderBase import *
from prophecy.cb.ui.uispec import *


class HtmlTable(MacroSpec):
    name: str = "HtmlTable"
    projectName: str = "test_sql_orch"
    category: str = "Transform"
    minNumOfInputPorts: int = 0


    @dataclass(frozen=True)
    class HtmlTableProperties(MacroProperties):
        title: str = ''
        tableName: str = ''
        columns: str = ''
        where: str = ''
        orderBy: str = ''
        limit: str = '100'
        caption: str = ''
        tableClass: str = 'dbt-table'
        includeIndex: str = 'true'
        summary: str = ''

    def dialog(self) -> Dialog:
        return Dialog("HtmlTable").addElement(
            ColumnsLayout(gap="1rem", height="100%")
            .addColumn(Ports(allowInputAddOrDelete=True), "content")
            .addColumn(
                StackLayout()
                .addElement(TextBox("Title").bindPlaceholder("Optional title above the table").bindProperty("title"))
                .addElement(TextBox("Table Name").bindPlaceholder("schema.table or database.schema.table").bindProperty("tableName"))
                .addElement(TextBox("Columns").bindPlaceholder("col1, col2, ... (blank = *)").bindProperty("columns"))
                .addElement(TextBox("Where").bindPlaceholder("status = 'active' AND dt >= '2025-01-01'").bindProperty("where"))
                .addElement(TextBox("Order By").bindPlaceholder("dt desc, id asc").bindProperty("orderBy"))
                .addElement(TextBox("Limit").bindPlaceholder("100").bindProperty("limit"))
                .addElement(TextBox("Caption").bindPlaceholder("Optional caption").bindProperty("caption"))
                .addElement(TextBox("Table CSS Class").bindPlaceholder("dbt-table").bindProperty("tableClass"))
                .addElement(TextBox("Include Index (true/false)").bindPlaceholder("true").bindProperty("includeIndex"))
                .addElement(TextBox("Summary footer mapping").bindPlaceholder("id:count,pct:avg,amount:sum").bindProperty("summary"))
            )
        )

    def validate(self, context: SqlContext, component: Component) -> List[Diagnostic]:
        # Validate the component's state
        return super().validate(context,component)

    def onChange(self, context: SqlContext, oldState: Component, newState: Component) -> Component:
        # Handle changes in the component's state and return the new state
        return newState

    def apply(self, props: HtmlTableProperties) -> str:
        def q(s: str) -> str:
            return '"' + s + '"'

        def html_escape(s: str) -> str:
            return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        relation = props.tableName
        if props.columns.strip():
            cols = [q(c.strip()) for c in props.columns.split(',') if c.strip()]
            columnsArg = "[" + ", ".join(cols) + "]"
        else:
            columnsArg = 'None'
        whereArg = q(props.where) if props.where.strip() else 'None'
        orderArg = q(props.orderBy) if props.orderBy.strip() else 'None'
        limitArg = props.limit.strip() if props.limit.strip() else '100'
        captionArg = q(props.caption) if props.caption.strip() else 'None'
        tableClassArg = q(props.tableClass) if props.tableClass.strip() else '"dbt-table"'
        includeIndexArg = 'true' if props.includeIndex.strip().lower() == 'true' else 'false'

        summaryArg = 'None'
        if props.summary.strip():
            pairs = [p.strip() for p in props.summary.split(',') if p.strip()]
            items = []
            for p in pairs:
                if ':' in p:
                    col, agg = [x.strip() for x in p.split(':', 1)]
                    if col and agg:
                        items.append('"' + col + '": "' + agg + '"')
            if items:
                summaryArg = '{' + ', '.join(items) + '}'

        # To avoid emitting raw HTML (<h2>...) directly (which may break SQL parsing),
        # we delegate the title rendering to concat_html_tables_from_relations with one section.
        sections = []
        title_str = props.title.strip() if props.title and props.title.strip() else ''
        # Build a JSON-like dict string for the single section
        # Mandatory relation
        section_parts = [
            '"title": ' + (q(title_str) if title_str else '""'),
            '"relation": ' + q(relation),
            '"columns": ' + columnsArg,
            '"where_clause": ' + whereArg,
            '"order_by": ' + orderArg,
            '"limit": ' + limitArg,
            '"caption": ' + captionArg,
            '"table_class": ' + tableClassArg,
            '"include_index": ' + includeIndexArg,
            '"summary": ' + summaryArg
        ]
        section_str = '{' + ', '.join(section_parts) + '}'
        sectionsArg = '[' + section_str + ']'
        resolved_macro_name = f"{self.projectName}.{self.name}"

        body = f"{{{{ {resolved_macro_name}({sectionsArg}) }}}}"
        return body
        #return "Select '" + body + "' as out_column"
    

    def loadProperties(self, properties: MacroProperties) -> PropertiesType:
        # load the component's state given default macro property representation
        parametersMap = self.convertToParameterMap(properties.parameters)
        return HtmlTable.HtmlTableProperties(
            title=parametersMap.get('title') or '',
            tableName=parametersMap.get('relation') or '',
            columns=parametersMap.get('columns') or '',
            where=parametersMap.get('where_clause') or '',
            orderBy=parametersMap.get('order_by') or '',
            limit=parametersMap.get('limit') or '100',
            caption=parametersMap.get('caption') or '',
            tableClass=parametersMap.get('table_class') or 'dbt-table',
            includeIndex=parametersMap.get('include_index') or 'true',
            summary=parametersMap.get('summary') or ''
        )

    def unloadProperties(self, properties: PropertiesType) -> MacroProperties:
        # convert component's state to default macro property representation
        return BasicMacroProperties(
            macroName=self.name,
            projectName=self.projectName,
            parameters=[
                MacroParameter("title", properties.title),
                MacroParameter("relation", properties.tableName),
                MacroParameter("columns", properties.columns),
                MacroParameter("where_clause", properties.where),
                MacroParameter("order_by", properties.orderBy),
                MacroParameter("limit", properties.limit),
                MacroParameter("caption", properties.caption),
                MacroParameter("table_class", properties.tableClass),
                MacroParameter("include_index", properties.includeIndex),
                MacroParameter("summary", properties.summary)
            ],
        )


