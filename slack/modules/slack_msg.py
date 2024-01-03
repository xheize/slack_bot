def db_unmatch_msg():
    msg_block = [{
        "color": "#FF385C",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "빌드 과정에서 DB 불일치를 발견하였습니다."
                }
            },
            {"type": "divider"},
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_preformatted",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Repo:{레포지토리 이름}\n"
                            },
                        ]
                    }
                ]
            },
            {"type": "divider"},
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "DB_Sync = True?"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Sync True",
                        "emoji": True
                    },
                    "value": "SyncTrue",
                    "action_id": "button-action"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "TypeORM Migration 기능 사용"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Migration",
                        "emoji": True
                    },
                    "value": "ORMMigrate",
                    "action_id": "button-action"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "DB_Sync = True?"
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Sync True",
                        "emoji": True
                    },
                    "value": "Ignore",
                    "action_id": "button-action"
                }
            },
            {"type": "divider"},
        ]
    }]
    return msg_block

