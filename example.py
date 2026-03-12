from autologger import setup_autologger

logger = setup_autologger()

print("This will go to the log file.")
print("Another message", 123)

logger.info("And this is from logger.info()")
