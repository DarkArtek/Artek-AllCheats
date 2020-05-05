from functools import wraps
import inspect, sims4.log
_normal_logger = sims4.log.LoggerClass('Interactions')
logger = _normal_logger

def unlock(target_function, new_function):

    @wraps(target_function)
    def _unlock(*args, **kwargs):
        logger.info('--B: {}'.format(target_function))
        return new_function(target_function, *args, **kwargs)

    logger.info('--A: {}'.format(target_function))
    return _unlock


def rewrite(target_object, target_function_name):

    def _rewrite(new_function):
        logger.info('A: {}'.format(target_function_name))
        target_function = getattr(target_object, target_function_name)
        logger.info('B: {}'.format(target_function_name))
        setattr(target_object, target_function_name, unlock(target_function, new_function))
        logger.info('C: {}'.format(target_function_name))

    logger.info('======Inject: {}'.format(target_function_name))
    return _rewrite