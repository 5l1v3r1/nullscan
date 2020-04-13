#!/usr/bin/env python3
# -*- coding: utf-8 -*- ########################################################
#               ____                     _ __                                  #
#    ___  __ __/ / /__ ___ ______ ______(_) /___ __                            #
#   / _ \/ // / / (_-</ -_) __/ // / __/ / __/ // /                            #
#  /_//_/\_,_/_/_/___/\__/\__/\_,_/_/ /_/\__/\_, /                             #
#                                           /___/ team                         #
#                                                                              #
# nullscan                                                                     #
# A modular framework designed to chain and automate security tests            #
#                                                                              #
# FILE                                                                         #
# telnet.py                                                                    #
#                                                                              #
# AUTHOR                                                                       #
# noptrix@nullsecurity.net                                                     #
#                                                                              #
################################################################################


# sys imports


# own imports
from modules.libs.base import Base, tool, timeout


class Telnet(Base):
  """ Telnet module (tcp/23) """


  def __init__(self, target, opts):
    """ init """

    Base.__init__(self, target, opts)

    return


  @tool
  def hydra_telnet(self):
    """
    DESCR: Bruteforce Telnet logins. (ext)
    TOOLS: hydra
    """

    opts = '-e nsr -f'
    self._hydra('telnet', opts)

    return


  @tool
  def nmap_telnet(self):
    """
    DESCR: Scan telnet service with corresponding NSE scripts. (ext)
    TOOLS: nmap
    """

    opts = '-n -sS -Pn --open --nsock-engine epoll'
    opts += ' --script telnet-encryption,telnet-ntlm-info'
    opts += f" -p {self.target['port']} {self.target['host']}"

    self._run_tool('nmap', opts, nullscan_tool='nmap_telnet')

    return


# EOF
