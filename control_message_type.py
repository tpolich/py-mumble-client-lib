__author__ = 'Tim'

import Mumble_pb2 as m

class ControlMessageType:

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
    
    @staticmethod
    def message(type):
        if type == ControlMessageType.VERSION:
            return m.Version
        if type == ControlMessageType.ACL:
            return m.ACL
        if type == ControlMessageType.AUTHENTICATE:
            return m.Authenticate
        if type == ControlMessageType.BAN_LIST:
            return m.BanList
        if type == ControlMessageType.CHANNEL_REMOVE:
            return m.ChannelRemove
        if type == ControlMessageType.CHANNEL_STATE:
            return m.ChannelState
        if type == ControlMessageType.CODEC_VERSION:
            return m.CodecVersion
        if type == ControlMessageType.CONTEXT_ACTION:
            return m.ContextAction
        if type == ControlMessageType.CONTEXT_ACTION_MODIFY:
            return m.ContextActionModify
        if type == ControlMessageType.CRYPT_SETUP:
            return m.CryptSetup
        if type == ControlMessageType.PERMISSION_DENIED:
            return m.PermissionDenied
        if type == ControlMessageType.PERMISSION_QUERY:
            return m.PermissionQuery
        if type == ControlMessageType.PING:
            return m.Ping
        if type == ControlMessageType.QUERY_USERS:
            return m.QueryUsers
        if type == ControlMessageType.REJECT:
            return m.Reject
        if type == ControlMessageType.REQUEST_BLOB:
            return m.RequestBlob
        if type == ControlMessageType.SERVER_CONFIG:
            return m.ServerConfig
        if type == ControlMessageType.SERVER_SYNC:
            return m.ServerSync
        if type == ControlMessageType.TEXT_MESSAGE:
            return m.TextMessage
        if type == ControlMessageType.SUGGEST_CONFIG:
            return m.SuggestConfig
        if type == ControlMessageType.UDP_TUNNEL:
            return m.UDPTunnel
        if type == ControlMessageType.USER_LIST:
            return m.UserList
        if type == ControlMessageType.USER_REMOVE:
            return m.UserRemove
        if type == ControlMessageType.VOICE_TARGET:
            return m.VoiceTarget
        if type == ControlMessageType.USER_STATS:
            return m.UserStats
        if type == ControlMessageType.USER_STATE:
            return m.UserState
        raise ValueError("No Matching Type For: " + type)