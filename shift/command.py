import numpy as np
import pandas as pd
from otlang.sdk.syntax import Keyword, Positional, OTLType
from pp_exec_env.base_command import BaseCommand, Syntax


class ShiftCommand(BaseCommand):
    # Shift index by desired number of periods
    """
    Shift index by desired number of periods.
    When period is not passed, shift index by 1.
    | shift a as b period=2, fill_value=0

    fill_value: The scalar value to use for newly introduced missing values.
    """
    syntax = Syntax(
        [
            Positional("column", required=True, otl_type=OTLType.TEXT),
            Keyword("period", required=False, otl_type=OTLType.INTEGER),
            Keyword("fill_value", required=False, otl_type=OTLType.INTEGER)
        ],
    )
    use_timewindow = False  # Does not require time window arguments
    idempotent = True  # Does not invalidate cache

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self.log_progress('Start shift command')
        # that is how you get arguments
        column_to_transform = self.get_arg("column").value
        new_column_name = self.get_arg("column").named_as
        period = self.get_arg("period").value or 1
        fill_value = self.get_arg("fill_value").value or 0

        self.logger.debug(f'Command shift get positional argument = {column_to_transform}')
        self.logger.debug(f"Command shift get period argument = {period}")
        self.logger.debug(f"Command shift get fill_value argument = {fill_value}")
        # logic here
        if new_column_name != "":
            df[new_column_name] = df[column_to_transform].shift(periods=period, fill_value=fill_value)

        else:
            df = pd.DataFrame(df[column_to_transform].shift(periods=period, fill_value=fill_value))

        self.log_progress('Shift command is completed.', stage=1, total_stages=1)
        return df
