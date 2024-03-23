import enum
from enum import Enum


class FakeNoticeType(Enum):
    NOTIFY_HAND_CARD_USE = 0
    NOTIFY_DRAW_COUNT = 1
    NOTIFY_DRAWN_CARD_LIST = 2
    NOTIFY_DECK_CARD_LIST_USE = 3
    NOTIFY_FIELD_UNIT_ENERGY = 4
    NOTIFY_SEARCH_COUNT = 5
    NOTIFY_SEARCH_CARD_LIST = 6
    NOTIFY_UNIT_SPAWN = 7

    NOTIFY_MULLIGAN_END = 22

    NOTIFY_BASIC_ATTACK_TO_UNIT = 1000
    NOTIFY_USE_FIELD_ENERGY_TO_UNIT = 1003
    NOTIFY_DEPLOY_UNIT = 1004
    NOTIFY_USE_UNIT_ENERGY_BOOST_SUPPORT_CARD = 1005
    NOTIFY_USE_INSTANT_UNIT_DEATH_ITEM_CARD = 1006
    NOTIFY_USE_CATASTROPHIC_DAMAGE_ITEM_CARD = 1007
    NOTIFY_USE_FIELD_ENERGY_REMOVE_SUPPORT_CARD = 1008
    NOTIFY_USE_FIELD_ENERGY_INCREASE_ITEM_CARD = 1009
    NOTIFY_USE_GENERAL_ENERGY_CARD_TO_UNIT = 1010
    NOTIFY_USE_SEARCH_DECK_SUPPORT_CARD = 1011
    NOTIFY_USE_SPECIAL_ENERGY_CARD_TO_UNIT = 1012
    NOTIFY_USE_DRAW_SUPPORT_CARD = 1013
    NOTIFY_USE_MULTIPLE_UNIT_DAMAGE_ITEM_CARD = 1014
    NOTIFY_USE_UNIT_ENERGY_REMOVE_ITEM_CARD = 1015
    NOTIFY_BASIC_ATTACK_TO_MAIN_CHARACTER = 1016

    NOTIFY_DEPLOY_TARGETING_ATTACK_PASSIVE_SKILL_TO_UNIT = 2000
    NOTIFY_DEPLOY_TARGETING_ATTACK_TO_GAME_MAIN_CHARACTER = 2001
    NOTIFY_DEPLOY_NON_TARGETING_ATTACK_PASSIVE_SKILL = 2002

    NOTIFY_TURN_START_TARGETING_ATTACK_PASSIVE_SKILL_TO_UNIT = 2010
    NOTIFY_TURN_START_TARGETING_ATTACK_TO_GAME_MAIN_CHARACTER = 2011
    NOTIFY_TURN_START_NON_TARGETING_ATTACK_PASSIVE_SKILL = 2012

