from py_mumble_lib import Mumble_pb2 as m

__author__ = 'Tim'

VERSION = 0
UDP_TUNNEL = 1
AUTHENTICATE = 2
PING = 3
REJECT = 4
SERVER_SYNC = 5
CHANNEL_REMOVE = 6
CHANNEL_STATE = 7
USER_REMOVE = 8
USER_STATE = 9
BAN_LIST = 10
TEXT_MESSAGE = 11
PERMISSION_DENIED = 12
ACL = 13
QUERY_USERS = 14
CRYPT_SETUP = 15
CONTEXT_ACTION_MODIFY = 16
CONTEXT_ACTION = 17
USER_LIST = 18
VOICE_TARGET = 19
PERMISSION_QUERY = 20
CODEC_VERSION = 21
USER_STATS = 22
REQUEST_BLOB = 23
SERVER_CONFIG = 24
SUGGEST_CONFIG = 25


def type_to_message(type):
    if type == VERSION:
        return m.Version
    if type == ACL:
        return m.ACL
    if type == AUTHENTICATE:
        return m.Authenticate
    if type == BAN_LIST:
        return m.BanList
    if type == CHANNEL_REMOVE:
        return m.ChannelRemove
    if type == CHANNEL_STATE:
        return m.ChannelState
    if type == CODEC_VERSION:
        return m.CodecVersion
    if type == CONTEXT_ACTION:
        return m.ContextAction
    if type == CONTEXT_ACTION_MODIFY:
        return m.ContextActionModify
    if type == CRYPT_SETUP:
        return m.CryptSetup
    if type == PERMISSION_DENIED:
        return m.PermissionDenied
    if type == PERMISSION_QUERY:
        return m.PermissionQuery
    if type == PING:
        return m.Ping
    if type == QUERY_USERS:
        return m.QueryUsers
    if type == REJECT:
        return m.Reject
    if type == REQUEST_BLOB:
        return m.RequestBlob
    if type == SERVER_CONFIG:
        return m.ServerConfig
    if type == SERVER_SYNC:
        return m.ServerSync
    if type == TEXT_MESSAGE:
        return m.TextMessage
    if type == SUGGEST_CONFIG:
        return m.SuggestConfig
    if type == UDP_TUNNEL:
        return m.UDPTunnel
    if type == USER_LIST:
        return m.UserList
    if type == USER_REMOVE:
        return m.UserRemove
    if type == VOICE_TARGET:
        return m.VoiceTarget
    if type == USER_STATS:
        return m.UserStats
    if type == USER_STATE:
        return m.UserState
    raise ValueError("No Matching Type For: " + type)