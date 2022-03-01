# -*- coding: utf-8 -*-
# telegram
USER_NAME = '@Karacsony'
API_ID = 17458144
API_HASH = 'c1de59310d3863bbe357b11241af88be'

# parser
EXTRA_WORDS = [
    'Silver', 'Bronze', 'Black',
    'Blue', 'Pink'
]
EXTRA_WORDS = [s.lower() for s in EXTRA_WORDS]

# debug
DEBUG = False

# handler
# recommendation for developer: use chat int id's
HANDLED_CHATS = {
    #mitrion chat
    -1001173851201: [631288367, 401959243,640495122],
    #mitrion fallback
    -1001381147394: [631288367, 401959243,640495122],
    # extractor test
    -409330338: [-409330338],
    # 1000 trifles A01
#    -1001449349991: [-1001255055406],
    #Alikson +79816841206
#    -1001394956746: [-1001255055406],
}

# etc
DATE_WITH_TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
DATE_FORMAT = '%Y-%m-%d'
