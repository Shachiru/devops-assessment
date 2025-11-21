#!/bin/bash
LOG_FILE="/opt/webapp/logs/monitor.log"
echo "=== Monitoring Report: $(date) ===" >> $LOG_FILE
echo "Memory Usage:" >> $LOG_FILE
free -h >> $LOG_FILE
echo "Disk Usage /opt/webapp:" >> $LOG_FILE
du -sh /opt/webapp/ >> $LOG_FILE
echo "App Status:" >> $LOG_FILE
systemctl is-active webapp >> $LOG_FILE
echo "Nginx Status:" >> $LOG_FILE
systemctl is-active nginx >> $LOG_FILE
echo "---------------------------------" >> $LOG_FILE