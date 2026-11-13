# AccountOds_Configuration
# Client-specific Account ODS configuration dictionaries.
#
# Each dictionary is named functions_<CLIENT_ID>.
# AccReadables points to that client's history table.
# UpsertOnAccData defines the matching key used by the Account ODS upsert.
#
# IMPORTANT:
# - These entries are transcribed from the supplied Databricks screenshots.
# - Verify spellings/table names against the live notebook before committing.
# - Client ID 24 (BCBSNE) uses its special UpsertOnAccDataBCBSNE method.

functions_174 = {
    'AccReadables': 'history.account_history_clearecare',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_123 = {
    'AccReadables': 'history.account_history_baycare',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_166 = {
    'AccReadables': 'history.account_history_goldkidney',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_144 = {
    'AccReadables': 'history.account_history_vivahealth',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_145 = {
    'AccReadables': 'history.account_history_optumcare',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_72 = {
    'AccReadables': 'history.account_history_chpca',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_117 = {
    'AccReadables': 'history.account_history_molina',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_131 = {
    'AccReadables': 'history.account_history_brandnewday',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_122 = {
    'AccReadables': 'history.account_history_careoregon',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_67 = {
    'AccReadables': 'history.account_history_bsca',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_66 = {
    'AccReadables': 'history.account_history_presbyterian',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_99 = {
    'AccReadables': 'history.account_history_geisinger',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_126 = {
    'AccReadables': 'history.account_history_securityhealth',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_40 = {
    'AccReadables': 'history.account_history_amerihealthmedicare',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_136 = {
    'AccReadables': 'history.account_history_bcbsaz',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_48 = {
    'AccReadables': 'history.account_history_healthfirst',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_23 = {
    'AccReadables': 'history.account_history_medigold',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_34 = {
    'AccReadables': 'history.account_history_iuhealth',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_96 = {
    'AccReadables': 'history.account_history_ucare',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_100 = {
    'AccReadables': 'history.account_history_highmark',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_103 = {
    'AccReadables': 'history.account_history_cdphp',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_111 = {
    'AccReadables': 'history.account_history_cloverhealth',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_77 = {
    'AccReadables': 'history.account_history_elderplan',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_80 = {
    'AccReadables': 'history.account_history_martinspoint',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_84 = {
    'AccReadables': 'history.account_history_essence',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_85 = {
    'AccReadables': 'history.account_history_harvardpilgrim',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_89 = {
    'AccReadables': 'history.account_history_quartz',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_90 = {
    'AccReadables': 'history.account_history_uphp',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_114 = {
    'AccReadables': 'history.account_history_healthnow',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_38 = {
    'AccReadables': 'history.account_history_healthplanuov',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_68 = {
    'AccReadables': 'history.account_history_healthnewengland',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_119 = {
    'AccReadables': 'history.account_history_iha',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_135 = {
    'AccReadables': 'history.account_history_fhcp',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_130 = {
    'AccReadables': 'history.account_history_aspire',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_143 = {
    'AccReadables': 'history.account_history_imperialhealth',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_141 = {
    'AccReadables': 'history.account_history_bcbsma',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_163 = {
    'AccReadables': 'history.account_history_zinghealth',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_64 = {
    'AccReadables': 'history.account_history_excellus',
    'UpsertOnAccData': {'condition': ['AccountID']}
}

functions_24 = {
    'AccReadables': 'history.account_history_bcbsne',
    'UpsertOnAccDataBCBSNE': {'condition': ['AccountID']}
}
