TOP = .
include $(TOP)/configure/CONFIG
DIRS += configure helloApp
helloApp_DEPEND_DIRS = configure
include $(TOP)/configure/RULES_TOP
