def timeit(method):
    """
        A decorator to report the time taken by a requested function.
    :param method:   method that needs to be considered
    :return:         method with recordings 'on'
    """
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r took %2.2f sec' % \
              (method.__name__, te-ts)
        return result
    return timed
