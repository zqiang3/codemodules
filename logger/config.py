#!/usr/bin/env python
# coding:utf-8


project_home = 'e:/test'
DEBUG = True

# 日志相关
LOG_CONFIG = {
	# format: dict
	# each item is a dict, contains 'name', 'path', 'level'
    # The log name is ID of a log.
    # The file path support both absolute path and relative path(relative to
    # `project_home` path).
    # The log levels provided are 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
	'debug':
		{
			'name': 'debug-log',
			'path': 'logs/flask-debug-log',
			'level': 'DEBUG'
		},
	'error':
		{
			'name': 'error-log',
			'path': 'logs/flask-error-log',
			'level': 'ERROR'
		}
}

LOG_OPER = {
	'name': 'error-report',
	'path': 'logs/error-report',
	'level': 'DEBUG'
}
