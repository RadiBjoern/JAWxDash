from dash import html
import logging

from src import ids

logger = logging.getLogger(__name__)


stat_table_layout = html.Div(
    id=ids.Div.STAT_TABLE,
)
