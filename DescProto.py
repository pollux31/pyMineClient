'''
Created on 17 juin 2014

@author: Thierry
'''
LOGIN_STATE = 0
PLAY_STATE = 1
STATUS_STATE = 2


# Packet definition Client -> Server
# ---------------------------------------------------------------------------
LOGIN_IN = {
            0x00 : {'name' : 'disconnect',
                    'func' : 'trtDisconnect',
                    'data' : ['json_data', 'String']},

            0x01 : {'name' : 'encryption_request',
                    'func' : None,
                    'data' : ['server_ID'   , 'String',
                             'length_public', 'Short',
                             'public_key'   , 'Bytearray|length_public',
                             'length_token' , 'Short',
                             'verify_token' , 'ByteArray|length_token']},
            
            0x02 : {'name' : 'login_success',
                    'trace': True,
                    'func' : 'trtLoginSuccess',
                    'data' : ['uuid'    , 'String',
                              'username', 'String']},

            }


# ---------------------------------------------------------------------------
LOGIN_OUT = {
             'login_start'  : [0x00,['name','String']],
             
             'handshake'    : [0x00,['protocol_version','Varint',
                                     'server_adress'   ,'String',
                                     'server_port'     ,'UShort',
                                     'next_state'      ,'Varint']],   

             'encryption_response' : [0x01,['lenght_public','Short',
                                            'share_secret' ,'ByteArray',
                                            'length_tocken','Short',
                                            'verify_token' ,'ByteArray']],   
        }




# ---------------------------------------------------------------------------
STATUS_IN = {}


# ---------------------------------------------------------------------------
STATUS_OUT = {}


# ---------------------------------------------------------------------------
PLAY_IN = {
            0x00 : {'name' : 'keep_alive',
                    'func' : 'trtKeepAlive',
                    'data' : ['keep_alive_id', 'Int']},

            0x01 : {'name' : 'join_game',
                    'trace': True,
                    'func' : 'trtJoinGame',
                    'data' : ['entity_id' , 'Int',
                              'gamemode'  , 'UByte',
                              'dimension' , 'Byte',
                              'difficulty', 'UByte',
                              'max_player', 'UByte',
                              'level_type', 'String']},
           
            0x02 : {'name' : 'chat_message',
                    'func' : 'trtChat',
                    'data' : ['json_data', 'String']},

            0x03 : {'name' : 'time_update',
                    'func' : None,
                    'data' : ['age_of_the_world', 'Long',
                              'time_of_day'     , 'Long']},

            0x04 : {'name' : 'entity_equipment',
                    'func' : None,
                    'trace': True,
                    'data' : ['entity_id', 'Int',
                              'slot'     , 'Short',
                              'item'     , 'Slot']},

            0x05 : {'name' : 'spawn_position',
                    'trace': True,
                    'func' : 'trtSpawn',
                    'data' : ['x', 'Int',
                              'y', 'Int',
                              'z', 'Int']},

            0x06 : {'name' : 'update_health',
                    'trace': True,
                    'func' : 'trtHealth',
                    'data' : ['health'         , 'Float',
                              'food'           , 'Short',
                              'food_saturation', 'Float']},

            0x07 : {'name' : 'respawn',
                    'trace': True,
                    'func' : None,
                    'data' : ['dimension' , 'Int',
                              'difficulty', 'UByte',
                              'gamemode'  , 'UByte'
                              'level_type', 'String']},

            0x08 : {'name' : 'player_position_and_look',
                    'trace': True,
                    'func' : 'trtPlayerPositinLook',
                    'data' : ['x'        , 'Double',
                              'y'        , 'Double',
                              'z'        , 'Double',
                              'yaw'      , 'Float',
                              'Pitch'    , 'Float',
                              'on_ground', 'Bool']},

            0x09 : {'name' : 'held_item_change',
                    'func' : None,
                    'data' : ['slot', 'Byte']},

            0x0A : {'name' : 'use_bed',
                    'func' : None,
                    'data' : ['entity_id', 'Int',
                              'x'        , 'Int',
                              'y'        , 'UByte',
                              'z'        , 'Int']},

            0x0B : {'name' : 'animation',
                    'func' : None,
                    'data' : ['entity_id', 'Int',
                              'animation', 'UByte']},

            0x0C : {'name' : 'spawn_player',
                    'trace': True,
                    'func' : 'trtSpawnPlayer',
                    'data' : ['entity_id'   , 'Varint',
                              'player_uuid' , 'String',
                              'player_name' , 'String',
                              'data_count'  , 'Varint',
                              'x'           , 'Int',
                              'y'           , 'Int',
                              'z'           , 'Int',
                              'yaw'         , 'Byte',
                              'pitch'       , 'Byte',
                              'current_item', 'Short',
                              'metadata'    , 'Metadata']},

            0x0D : {'name' : 'collect_item',
                    'func' : None,
                    'data' : ['collected_entity_id', 'Int',
                              'collector_entity_id', 'Int']},

            0x0E : {'name' : 'spawn_object',
                    'func' : None,
                    'data' : ['entity_id', 'Varint',
                              'type'     , 'Byte',
                              'x'        , 'Int',
                              'y'        , 'Int', 
                              'z'        , 'Int', 
                              'pitch'    , 'Byte',
                              'yaw'      , 'Byte',
                              'data'     , 'ObjectData']}, # TODO: write function
           
            0x0F : {'name' : 'spawn_mob',
                    'trace': True,
                    'func' : None,
                    'data' : ['entity_id', 'Varint',
                              'type'     , 'UByte',
                              'x'        , 'Int',
                              'y'        , 'Int',
                              'z'        , 'Int',
                              'yaw'      , 'Byte',
                              'pitch'    , 'Byte',
                              'health_pitch', 'Byte',
                              'velocity_x'  , 'Short',
                              'velocity_y'  , 'Short',
                              'velocity_z'  , 'Short',
                              'metadata'    , 'Metadata']},

            0x10 : {'name' : 'spawn_painting',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x11 : {'name' : 'spawn_experience_orb',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x12 : {'name' : 'entity_velocity',
                    'trace': True,
                    'func' : None,
                    'data' : ['entity_id' , 'Int',
                              'velocity_x', 'Byte',
                              'velocity_y', 'Byte',
                              'velocity_z', 'Byte']},

            0x13 : {'name' : 'destroy_entity',
                    'trace': True,
                    'func' : None,
                    'data' : ['count'     , 'Byte',
                              'entity_ids', 'Intarray|count']},

            0x14 : {'name' : 'entity',
                    'trace': True,
                    'func' : 'trtEntity',
                    'data' : ['entity_id' , 'Int']},

            0x15 : {'name' : 'entity_relative_move',
                    'trace': True,
                    'func' : 'trtEntityRelativeMove',
                    'data' : ['entity_id', 'Int',
                              'dx'       , 'Byte',
                              'dy'       , 'Byte',
                              'dz'       , 'Byte']},
           
            0x16 : {'name' : 'entity_look',
                    'trace': True,
                    'func' : 'trtEntityLook',
                    'data' : ['entity_id', 'Int',
                              'yaw'      , 'Byte',
                              'pitch'    , 'Byte']},
           
            0x17 : {'name' : 'entity_look_and_relative_move',
                    'trace': True,
                    'func' : 'trtEntityLookMove',
                    'data' : ['entity_id', 'Int',
                              'dx'       , 'Byte',
                              'dy'       , 'Byte',
                              'dz'       , 'Byte',
                              'yaw'      , 'Byte',
                              'pitch'    , 'Byte']},
 
            0x18 : {'name' : 'entity_teleport',
                    'trace': True,
                    'func' : 'trtEntityTeleport',
                    'data' : ['entity_id', 'Int',
                              'x'        , 'Int',
                              'y'        , 'Int',
                              'z'        , 'Int',
                              'yaw'      , 'Byte',
                              'pitch'    , 'Byte']},
 
            0x19 : {'name' : 'entity_head_look',
                    'trace': True,
                    'func' : None,
                    'data' : ['entity_id', 'Int',
                              'head_yaw' , 'Byte']},

            0x1A : {'name' : 'entity_status',
                    'trace': True,
                    'func' : None,
                    'data' : ['entity_id'    , 'Int',
                              'entity_status', 'Byte']},

            0x1B : {'name' : 'attach_entity',
                    'trace': True,
                    'func' : None,
                    'data' : ['entity_id' , 'Int',
                              'vehicle_id', 'Int',
                              'leash'     , 'Bool']},

            0x1C : {'name' : 'entity_metadata',
                    'trace': True,
                    'func' : None,
                    'data' : ['entity_id', 'Int',
                              'metadata' , 'Metadata']},

            0x1D : {'name' : 'entity_effect',
                    'trace': True,
                    'func' : None,
                    'data' : ['entity_id' ,'Int',
                              'effect_id', 'Byte',
                              'amplifier', 'Byte',
                              'duration' , 'Short']},

            0x1E : {'name' : 'remove_entity_effect',
                    'trace': True,
                    'func' : None,
                    'data' : ['entity_id', 'Int',
                              'effect_id', 'Byte']},

            0x1F : {'name' : 'set_experience',
                    'trace': True,
                    'func' : None,
                    'data' : ['experience_bar'  , 'Float',
                              'level'           , 'Short',
                              'total_experience', 'Short']},

            0x20 : {'name' : 'entity_properties',
                    'trace': True,
                    'func' : None,
                    'data' : ['entity_id', 'Int',
                              'count' , 'Int',
                              'properties', 'PropertyArray|count']},

            0x21 : {'name' : 'chunk_data',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x22 : {'name' : 'multi_bloc_change',
                    'trace': False,
                    'func' : None,
                    'data' : []},
           
            0x23 : {'name' : 'block_change',
                    'trace': False,
                    'func' : None,
                    'data' : []},
           
            0x24 : {'name' : 'block_action',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x25 : {'name' : 'block_break_animation',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x26 : {'name' : 'map_chunk_bulk',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x27 : {'name' : 'explosion',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x28 : {'name' : 'effect',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x29 : {'name' : 'sound_effect',
                    'trace': False,
                    'func' : None,
                    'data' : []},
           
            0x2A : {'name' : 'particle',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x2B : {'name' : 'change_game_state',
                    'trace': False,
                    'func' : None,
                    'data' : []},
           
            0x2C : {'name' : 'spawn_global_entity',
                    'trace': True,
                    'func' : 'trtSpawnGlobalEntity',
                    'data' : ['entity_id', 'Varint',
                              'type'     , 'Byte',
                              'x'        , 'Int',
                              'y'        , 'Int',
                              'z'        , 'Int']},
           
            0x2D : {'name' : 'open_window',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x2E : {'name' : 'cloase_window',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x2F : {'name' : 'set_slot',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x30 : {'name' : 'window_item',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x31 : {'name' : 'window_property',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x32 : {'name' : 'confirm_transaction',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x33 : {'name' : 'update_sign',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x34 : {'name' : 'maps',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x35 : {'name' : 'update_block_entity',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x36 : {'name' : 'sign_editor_open',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x37 : {'name' : 'statistics',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x38 : {'name' : 'player_list_item',
                    'trace': True,
                    'func' : None,
                    'data' : ['player_name', 'String',
                              'online', 'Bool',
                              'ping','Short']},
           
            0x39 : {'name' : 'player_abilities',  # TODO: store these information in the player class
                    'trace': True,
                    'func' : None,
                    'data' : ['flags', 'Byte',
                              'flying_speed', 'Float',
                              'walking_speed', 'Float']},
           
            0x3A : {'name' : 'tab_complete',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x3B : {'name' : 'scoreboard_objective',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x3C : {'name' : 'update_score',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x3D : {'name' : 'display_score',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x3E : {'name' : 'teams',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x3F : {'name' : 'plugin message',
                    'trace': True,
                    'func' : None,
                    'data' : []},
           
            0x40 : {'name' : 'disconnect',
                    'trace': True,
                    'func' : None,                  # TODO: take Disconnect in account
                    'data' : ['reason', 'String']},
           
           }


# ---------------------------------------------------------------------------
PLAY_OUT = {
            'keep_alive'    : [0x00, ['keep_alive_id', 'Int']],
            
            'chat_message'  : [0x01, ['message', 'String']],
             
            'use_entity'    : [0x02, ['target', 'Int',
                                      'mouse' , 'Byte']],
             
            'player'        : [0x03, ['on_ground', 'Bool']],
             
            'player_position' : [0x04, ['x'        , 'Double',
                                        'feet_y'   , 'Double',
                                        'head_y'   , 'Double',
                                        'z'        , 'Double',
                                        'on_ground', 'Bool']],
             
            'player_look'   : [0x05, ['yaw'      , 'Float',
                                      'pitch'    , 'Float',
                                      'on_ground', 'Bool']],
             
            'player_position_and_look' : [0x06, ['x'        , 'Double',
                                                 'feet_y'   , 'Double',
                                                 'head_y'   , 'Double',
                                                 'z'        , 'Double',
                                                 'yaw'      , 'Float',
                                                 'pitch'    , 'Float',
                                                 'on_ground', 'Bool']],
             
            'player_digging' : [0x07, ['status', 'Byte',
                                       'x'     , 'Int',
                                       'y'     , 'UByte',
                                       'z'     , 'Int',
                                       'face'  , 'Byte']],
             
            'player_bloc_placement' : [0x08, ['x'                , 'Int',
                                              'y'                , 'UByte',
                                              'z'                , 'Int',
                                              'direction'        , 'Byte',
                                              'held_item'        , 'Slot',
                                              'cursor_position_x', 'Byte',
                                              'cursor_position_y', 'Byte',
                                              'cursor_position_z', 'Byte']],
             
            'held_item_change' : [0x09, ['slot', 'Slot']],
             
            'animation'        : [0x0A, ['entity_id', 'Int',
                                         'animation', 'Byte']],
             
            'entity_action'    : [0x0B, ['entity_id' , 'Int',
                                         'action_id' , 'Byte',
                                         'jump_boost', 'Int']],
             
            'ster_vehicle'     : [0x0C, ['sideways', 'Float',
                                         'forward' , 'Float',
                                         'jump'    , 'Bool',
                                         'unmount' , 'Bool']],
             
            'close_window'     : [0x0D, ['window_id', 'Byte']],
             
            'click_window'     : [0x0E, ['window_id'    , 'Byte',
                                         'slot'         , 'Short',
                                         'button'       , 'Byte',
                                         'action_number', 'Short',
                                         'mode'         , 'Byte',
                                         'clicked_item' , 'Slot']],
             
            'confirm_transaction' : [0x0F, ['window_id'    , 'Byte',
                                            'action_number', 'Short',
                                            'accpeted'     , 'Bool']],
             
            'creative_inventory_action' : [0x10, ['slot'        , 'Short',
                                                  'clicked_item', 'Slot']],
             
            'enchant_item'     : [0x11, ['window_id'  , 'Byte',
                                         'enchantment', 'Byte']],
             
            'update_sign'      : [0x12, ['x', 'Int',
                                         'y', 'Short',
                                         'z', 'Int',
                                         'lien_1', 'String',
                                         'lien_2', 'String',
                                         'lien_3', 'String',
                                         'lien_4', 'String']],
             
            'player_abilities' : [0x13, ['flags'        , 'Byte',
                                         'flying_speed' , 'Float',
                                         'walking_speed', 'Float']],
             
            'tab_complete'     : [0x14, ['text', 'String']],
             
            'client_settings'  : [0x15, ['locale', 'String',
                                         'view_distance', 'Byte',
                                         'chat flags'   , 'Byte',
                                         'chat colours' , 'Bool',
                                         'difficulty'   , 'Byte',
                                         'show_cape'    , 'Bool']],
             
            'client_status'    : [0x16, ['action_id', 'Byte']],    # TODO: Send this command after login
             
            'plugin_message'   : [0x17, ['chanel', 'String',
                                         'length', 'Short',
                                         'data'  , 'Bytearray']],
             
            }

