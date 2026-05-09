# Base Bot Class

import logging
from abc import ABC, abstractmethod


class BaseBot(ABC):
    """Base class for all social media bots"""
    
    def __init__(self, platform_name):
        self.platform_name = platform_name
        self.logger = logging.getLogger(f"Bot.{platform_name}")
        self.is_running = False
    
    @abstractmethod
    def authenticate(self):
        """Authenticate with the social media platform"""
        pass
    
    @abstractmethod
    def start(self):
        """Start the bot"""
        pass
    
    @abstractmethod
    def stop(self):
        """Stop the bot"""
        pass
    
    def log_action(self, action):
        """Log bot action"""
        self.logger.info(f"[{self.platform_name}] {action}")
    
    def log_error(self, error):
        """Log bot error"""
        self.logger.error(f"[{self.platform_name}] {error}")
