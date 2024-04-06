from rest_framework.throttling import UserRateThrottle
import logging

# Configure logger
logger = logging.getLogger(__name__)

class ReadRateThrottle(UserRateThrottle):
    scope = 'read'

class WriteRateThrottle(UserRateThrottle):
    scope = 'write'

try:
    logger.info("Throttle classes ReadRateThrottle and WriteRateThrottle loaded successfully.")
except Exception as e:
    logger.error("Error loading throttle classes: %s", e, exc_info=True)