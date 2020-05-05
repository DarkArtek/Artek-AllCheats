import server_commands, sims4.commands
from sims4.commands import Command, CommandType, CommandRestrictionFlags
import PublicUnlock, services
from server_commands.argument_helpers import TunableInstanceParam
import sims4.log
_normal_logger = sims4.log.LoggerClass('Interactions')
logger = _normal_logger
with sims4.reload.protected(globals()):
    is_command_available = lambda command_type: True
import inspect, re
REMOVE_ACCOUNT_ARG = re.compile('(, ?)?_account=None', flags=(re.IGNORECASE))