import logging
import os
import sys

import deepsecurity
import urllib3
from crhelper import CfnResource
from deepsecurity.rest import ApiException

logger = logging.getLogger(__name__)

def lambda_handler(event, context):
  logger.info(event)
  logger.info(context)
