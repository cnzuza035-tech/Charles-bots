# Task Scheduler Module

import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from config import SCHEDULE_ENABLED, CHECK_INTERVAL

logger = logging.getLogger('CharlesBots.Scheduler')


class BotScheduler:
    """Bot task scheduler"""
    
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.is_running = False
    
    def start(self):
        """Start the scheduler"""
        if SCHEDULE_ENABLED:
            self.scheduler.start()
            self.is_running = True
            logger.info("Scheduler started")
    
    def stop(self):
        """Stop the scheduler"""
        if self.is_running:
            self.scheduler.shutdown()
            self.is_running = False
            logger.info("Scheduler stopped")
    
    def add_job(self, func, trigger, **kwargs):
        """Add a scheduled job"""
        self.scheduler.add_job(func, trigger, **kwargs)
    
    def add_cron_job(self, func, cron_expression):
        """Add a cron-based job"""
        trigger = CronTrigger.from_crontab(cron_expression)
        self.scheduler.add_job(func, trigger)
