#!/usr/bin/env python3
from bot import CMD_SUFFIX, config_dict

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'mirror1{CMD_SUFFIX}', f'm1{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'qbmirror1{CMD_SUFFIX}', f'qm1{CMD_SUFFIX}']
        self.YtdlCommand = [f'ytdl1{CMD_SUFFIX}', f'y1{CMD_SUFFIX}']
        self.LeechCommand = [f'leech1{CMD_SUFFIX}', f'l1{CMD_SUFFIX}']
        self.QbLeechCommand = [f'qbleech1{CMD_SUFFIX}', f'ql1{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdlleech1{CMD_SUFFIX}', f'yl1{CMD_SUFFIX}']
        if config_dict['SHOW_EXTRA_CMDS']:
            self.MirrorCommand.extend([f'unzipmirror1{CMD_SUFFIX}', f'uzm1{CMD_SUFFIX}', f'zipmirror1{CMD_SUFFIX}', f'zm1{CMD_SUFFIX}'])
            self.QbMirrorCommand.extend([f'qbunzipmirror1{CMD_SUFFIX}', f'quzm1{CMD_SUFFIX}', f'qbzipmirror1{CMD_SUFFIX}', f'qzm1{CMD_SUFFIX}'])
            self.YtdlCommand.extend([f'ytdlzip{CMD_SUFFIX}', f'yz{CMD_SUFFIX}'])
            self.LeechCommand.extend([f'unzipleech1{CMD_SUFFIX}', f'uzl1{CMD_SUFFIX}', f'zipleech1{CMD_SUFFIX}', f'zl1{CMD_SUFFIX}'])
            self.QbLeechCommand.extend([f'qbunzipleech1{CMD_SUFFIX}', f'quzl1{CMD_SUFFIX}', f'qbzipleech1{CMD_SUFFIX}', f'qzl1{CMD_SUFFIX}'])
            self.YtdlLeechCommand.extend([f'ytdlzipleech{CMD_SUFFIX}', f'yzl{CMD_SUFFIX}'])
        self.CloneCommand = [f'clone1{CMD_SUFFIX}', f'c1{CMD_SUFFIX}']
        self.CountCommand = f'count1{CMD_SUFFIX}'
        self.DeleteCommand = f'del1{CMD_SUFFIX}'
        self.CancelMirror = f'cancel1{CMD_SUFFIX}'
        self.CancelAllCommand = [f'cancelall1{CMD_SUFFIX}', 'cancellallbot']
        self.ListCommand = f'list1{CMD_SUFFIX}'
        self.SearchCommand = f'search1{CMD_SUFFIX}'
        self.StatusCommand = [f'status1{CMD_SUFFIX}', f's1{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'users1{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'authorize1{CMD_SUFFIX}', f'a{CMD_SUFFIX}']
        self.UnAuthorizeCommand = [f'unauthorize1{CMD_SUFFIX}', f'ua1{CMD_SUFFIX}']
        self.AddBlackListCommand = [f'blacklist1{CMD_SUFFIX}', f'bl1{CMD_SUFFIX}']
        self.RmBlackListCommand = [f'rmblacklist1{CMD_SUFFIX}', f'rbl1{CMD_SUFFIX}']
        self.AddSudoCommand = f'addsudo1{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo1{CMD_SUFFIX}'
        self.PingCommand = [f'ping1{CMD_SUFFIX}', f'p1{CMD_SUFFIX}']
        self.RestartCommand = [f'restart1{CMD_SUFFIX}', f'r1{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = [f'stats1{CMD_SUFFIX}', f'st1{CMD_SUFFIX}']
        self.HelpCommand = f'help1{CMD_SUFFIX}'
        self.LogCommand = f'log1{CMD_SUFFIX}'
        self.ShellCommand = f'shell1{CMD_SUFFIX}'
        self.EvalCommand = f'eval1{CMD_SUFFIX}'
        self.ExecCommand = f'exec1{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals1{CMD_SUFFIX}'
        self.BotSetCommand = [f'bsetting1{CMD_SUFFIX}', f'bs1{CMD_SUFFIX}']
        self.UserSetCommand = [f'usetting1{CMD_SUFFIX}', f'us1{CMD_SUFFIX}']
        self.BtSelectCommand = f'btsel1{CMD_SUFFIX}'
        self.CategorySelect = f'ctsel1{CMD_SUFFIX}'
        self.SpeedCommand = [f'speedtest1{CMD_SUFFIX}', f'sp1{CMD_SUFFIX}']
        self.RssCommand = f'rss1{CMD_SUFFIX}'
        self.LoginCommand = 'login'
        self.AddImageCommand = f'addimg1{CMD_SUFFIX}'
        self.ImagesCommand = f'images1{CMD_SUFFIX}'
        self.IMDBCommand = f'imdb1{CMD_SUFFIX}'
        self.AniListCommand = f'anime1{CMD_SUFFIX}'
        self.AnimeHelpCommand = f'animehelp1{CMD_SUFFIX}'
        self.MediaInfoCommand = [f'mediainfo1{CMD_SUFFIX}', f'mi{CMD_SUFFIX}']
        self.MyDramaListCommand = f'mdl1{CMD_SUFFIX}'
        self.GDCleanCommand = [f'gdclean1{CMD_SUFFIX}', f'gc1{CMD_SUFFIX}']
        self.BroadcastCommand = [f'broadcast1{CMD_SUFFIX}', f'bc1{CMD_SUFFIX}']

BotCommands = _BotCommands()
