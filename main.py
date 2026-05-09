#!/usr/bin/env python3
"""
Charles Bots - Multi-Platform Social Media Bot Application
Main entry point for the bot application
"""

import sys
import logging
from datetime import datetime
from config import LOG_LEVEL, LOG_FILE
from utils.logger import setup_logger

# Setup logging
logger = setup_logger(LOG_LEVEL, LOG_FILE)


def print_banner():
    """Print welcome banner"""
    banner = """
    ╔═══════════════════════════════════════════════╗
    ║        CHARLES BOTS - Social Media Bot       ║
    ║     Multi-Platform Automation Framework      ║
    ║                 v1.0.0                       ║
    ╚═══════════════════════════════════════════════╝
    """
    print(banner)
    logger.info("Charles Bots started at " + datetime.now().isoformat())


def load_bots():
    """Load and initialize bot modules"""
    bots = {}
    
    try:
        from config import (
            ENABLE_INSTAGRAM, ENABLE_TWITTER, ENABLE_TIKTOK,
            ENABLE_FACEBOOK, ENABLE_LINKEDIN
        )
        
        if ENABLE_INSTAGRAM:
            logger.info("Loading Instagram bot...")
            try:
                from bots.instagram import InstagramBot
                bots['instagram'] = InstagramBot()
                logger.info("✓ Instagram bot loaded successfully")
            except Exception as e:
                logger.error(f"✗ Failed to load Instagram bot: {e}")
        
        if ENABLE_TWITTER:
            logger.info("Loading Twitter bot...")
            try:
                from bots.twitter import TwitterBot
                bots['twitter'] = TwitterBot()
                logger.info("✓ Twitter bot loaded successfully")
            except Exception as e:
                logger.error(f"✗ Failed to load Twitter bot: {e}")
        
        if ENABLE_TIKTOK:
            logger.info("Loading TikTok bot...")
            try:
                from bots.tiktok import TikTokBot
                bots['tiktok'] = TikTokBot()
                logger.info("✓ TikTok bot loaded successfully")
            except Exception as e:
                logger.error(f"✗ Failed to load TikTok bot: {e}")
        
        if ENABLE_FACEBOOK:
            logger.info("Loading Facebook bot...")
            try:
                from bots.facebook import FacebookBot
                bots['facebook'] = FacebookBot()
                logger.info("✓ Facebook bot loaded successfully")
            except Exception as e:
                logger.error(f"✗ Failed to load Facebook bot: {e}")
        
        if ENABLE_LINKEDIN:
            logger.info("Loading LinkedIn bot...")
            try:
                from bots.linkedin import LinkedInBot
                bots['linkedin'] = LinkedInBot()
                logger.info("✓ LinkedIn bot loaded successfully")
            except Exception as e:
                logger.error(f"✗ Failed to load LinkedIn bot: {e}")
    
    except ImportError as e:
        logger.error(f"Failed to load bots: {e}")
        return {}
    
    return bots


def run_bots(bots):
    """Run all loaded bots"""
    if not bots:
        logger.warning("No bots loaded. Please check configuration.")
        return
    
    logger.info(f"Starting {len(bots)} bot(s)...")
    
    try:
        for bot_name, bot_instance in bots.items():
            logger.info(f"Starting {bot_name} bot...")
            try:
                if hasattr(bot_instance, 'start'):
                    bot_instance.start()
                else:
                    logger.warning(f"{bot_name} bot does not have start method")
            except Exception as e:
                logger.error(f"Error running {bot_name} bot: {e}")
    
    except KeyboardInterrupt:
        logger.info("\nShutting down bots...")
        for bot_name, bot_instance in bots.items():
            try:
                if hasattr(bot_instance, 'stop'):
                    bot_instance.stop()
            except Exception as e:
                logger.error(f"Error stopping {bot_name} bot: {e}")
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


def main():
    """Main application entry point"""
    print_banner()
    
    logger.info("Loading configuration...")
    try:
        from config import USE_PROXY, PROXY_LIST
        if USE_PROXY and PROXY_LIST:
            logger.info(f"Using {len(PROXY_LIST)} proxy/proxies")
    except Exception as e:
        logger.error(f"Failed to load configuration: {e}")
        sys.exit(1)
    
    # Load bots
    bots = load_bots()
    
    if not bots:
        logger.warning("No bots were successfully loaded.")
        logger.info("Please check your configuration and try again.")
        sys.exit(1)
    
    # Run bots
    run_bots(bots)


if __name__ == "__main__":
    main()
