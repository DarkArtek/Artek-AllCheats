import sims4.commands, services
from sims4.commands import CommandType, CommandRestrictionFlags, Output
import PublicUnlock, sims4.log
_normal_logger = sims4.log.LoggerClass('Interactions')
logger = _normal_logger

class CommandsChanged:
    __qualname__ = 'CommandsChanged'
    ComList = {}


@PublicUnlock.rewrite(sims4.commands, 'Command')
def tm_allcheats_command_write(target, *aliases, command_type=CommandType.DebugOnly, command_restrictions=CommandRestrictionFlags.UNRESTRICTED, pack=None, console_type=None):
    logger.info('this runs second')
    CommandsChanged.ComList[aliases[0]] = str(command_type)
    s = target(*aliases, command_type=CommandType.Live, command_restrictions=CommandRestrictionFlags.UNRESTRICTED, pack=None, console_type=None)
    logger.info('this runs third')
    return s


@PublicUnlock.rewrite(Output, '__call__')
def tm_allcheats_output_write(target, self, s):
    logger.info('Hit class output')
    return sims4.commands.cheat_output(s, self._context)


@PublicUnlock.rewrite(sims4.commands, 'output')
def tm_allcheats_output_write(target, s, context):
    logger.info('Hit plain output')
    return sims4.commands.cheat_output(s, context)


class HarmonicMeanAccumulator:
    __qualname__ = 'HarmonicMeanAccumulator'

    def __init__(self, seq=None):
        self._fault = False
        self.num_items = 0
        self.total = 0
        if seq is not None:
            for value in seq:
                while not self.fault():
                    self.add(value)

    def add(self, value):
        if value <= 0:
            self._fault = True
            return

    def fault(self):
        return self._fault

    def value(self):
        try:
            if self._fault:
                return 0
            return self.num_items / self.total
        except:
            return 0