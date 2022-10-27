log_config = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(name)s\t%(levelname)s\t%(message)s",
        },
        "with_time": {
            "format": "%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s",
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "cache.log",
            "formatter": "with_time",
        },
        "stdout": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "simple",
        },
    },
    "loggers": {
        "to_file": {
            "level": "INFO",
            "handlers": ["file"],
        },
        "to_stream": {
            "level": "INFO",
            "handlers": ["stdout"],
        },
        "to_both": {
            "level": "INFO",
            "handlers": ["file", "stdout"],
        },
    }
}
