#!/usr/bin/env python
# coding:utf-8
# author: gzzhangqiang2014
# date: 2015-08-06


import logging
import sys
import time
import config
from config import LOG_CONFIG
from config import LOG_OPER

# 新建日志对象，返回
def get_logger(log_name, log_path, log_level, log_format):
	try:
		logger = logging.getLogger(log_name)
		handler = logging.FileHandler(log_path, 'a')
		handler.setFormatter(log_format)
		logger.addHandler(handler)
		logger.setLevel(log_level)
		return logger
	except Exception, e:
		return None


def get_date():
	return time.strftime('%Y-%m-%d', time.localtime())

# mark function name, file name, line
def declog(text, up):
	c = sys._getframe(up+1)
	text = '%s ([FUNCTION:%s] [FILE:%s] [LINE:%s])' % (text, c.f_code.co_name, c.f_code.co_filename, c.f_lineno)
	return text

# 标准日志类(常用)
class Log(object):
	logger = {}
	DEBUG = config.DEBUG

	# 初始化日志对象
	@staticmethod
	def init_log():
		Log.logger = {}
		for key, c in LOG_CONFIG.iteritems():
			log_name = key + '_' + get_date()
			if log_name not in Log.logger:
				log_format = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
				log_level = getattr(logging, c.get('level'))
				log_path = c.get('path') + '_' + get_date()
				log_path = config.project_home + '/' + log_path
				Log.logger[log_name] = get_logger(log_name, log_path, log_level, log_format)

	# 根据类型(debug or error)获取日志句柄
	@staticmethod
	def get_local_logger(type):
		try:
			log_key = "%s_%s" % (type, get_date())
			# 指定日期的日志对象不存在时，新建日志对象
			if log_key not in Log.logger:
				Log.init_log()
			local_logger = None
			for key, logger in Log.logger.iteritems():
				if type in key:
					local_logger = logger
					break
			return local_logger
		except Exception, e:
			return None

	@staticmethod
	def critical(text, up=1):
		try:
			local_logger = Log.get_local_logger('error')
			if local_logger:
				local_logger.critical(declog(text, up))
		except Exception, e:
			return

	@staticmethod
	def error(text, up=1):
		try:
			local_logger = Log.get_local_logger('error')
			if local_logger:
				local_logger.error(declog(text, up))
		except Exception, e:
			return

	@staticmethod
	def warn(text, up=1):
		try:
			local_logger = Log.get_local_logger('error')
			if local_logger:
				local_logger.warn(declog(text, up))
		except Exception, e:
			return

	@staticmethod
	def debug(text, up=1):
		if not Log.DEBUG:
			return

		try:
			local_logger = Log.get_local_logger('debug')
			if local_logger:
				local_logger.debug(declog(text, up))
		except Exception, e:
			return

	@staticmethod
	def debug_ex(msg_format, l_params, up = 1):
		if not Log.DEBUG:
			return

		try:
			local_logger = Log.get_local_logger('debug')
			if local_logger:
				strMsg = msg_format % l_params
				local_logger.debug(declog(strMsg, up))
		except Exception, e:
			return

	@staticmethod
	def info(text, up=1):
		try:
			local_logger = Log.get_local_logger('debug')
			if local_logger:
				local_logger.info(declog(text, up))
		except Exception, e:
			return

# 扩展日志类(扩展用途)
class LogOper(object):
	logger = {}

	@staticmethod
	def get_local_logger(type):
		try:
			log_key = "%s_%s" % (type, get_date())
			if log_key not in LogOper.logger:
				LogOper.init_log()
			local_logger = None
			for key, logger in LogOper.logger.iteritems():
				if type in key:
					local_logger = logger
					break
			return local_logger
		except Exception, e:
			return None

	@staticmethod
	def init_log():
		LogOper.logger = {}
		log_name = LOG_OPER.get('name') + '_' + get_date()
		if log_name not in LogOper.logger:
			log_format = logging.Formatter('[%(asctime)s],%(message)s', '%Y-%m-%d %H:%M:%S')
			log_level = getattr(logging, LOG_OPER.get('level'))
			log_path = LOG_OPER.get('path') + '_' + get_date()
			log_path = config.project_home + '/' + log_path
			LogOper.logger[log_name] = get_logger(log_name, log_path, log_level, log_format)

	@staticmethod
	def info(text, up=1):
		try:
			local_logger = LogOper.get_local_logger(LOG_OPER.get('name'))
			if local_logger:
				local_logger.info(text)
		except Exception, e:
			return

# 使用前新建日志目录: config.project_home+'/logs'
if __name__ == '__main__':
	Log.critical('critical log')
	Log.error('error log')
	Log.warn('warn log')
	Log.debug('debug log')
	Log.debug_ex('debug log %s', 'zq')
	Log.info('info log')
