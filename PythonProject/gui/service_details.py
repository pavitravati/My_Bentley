service_requirements = {
    "Demo Mode": {
        "requirements": {
            "needs_vehicle": False,
            "has_preconditions": False,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": False, "phone": True, "country": True
        }
    },

    "Customer Enrollment": {
        "requirements": {
            "needs_vehicle": False,
            "has_preconditions": True,
            "reason_for_block": "Not finished",
            "region_locks": []
        },
        "fields": {
            "name": True, "email": True, "password": True, "pin": True,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Add VIN": {
        "requirements": {
            "needs_vehicle": False,
            "has_preconditions": False,
            "reason_for_block": "Not finished",
            "region_locks": []
        },
        "fields": {
            "name": True, "email": True, "password": True, "pin": True,
            "vin": True, "vehicle": True, "phone": True, "country": True
        }
    },

    "App Registration Pages": {
        "requirements": {
            "needs_vehicle": False,
            "has_preconditions": False,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": True, "vehicle": False, "phone": True, "country": True
        }
    },

    "App Log in-Log out": {
        "requirements": {
            "needs_vehicle": False,
            "has_preconditions": True,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": True, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Nickname": {
        "requirements": {
            "needs_vehicle": False,
            "has_preconditions": False,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Services and licenses": {
        "requirements": {
            "needs_vehicle": False,
            "has_preconditions": False,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Vehicle Status Report": {
        "requirements": {
            "needs_vehicle": True,
            "has_preconditions": True,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Remote Lock-Unlock": {
        "requirements": {
            "needs_vehicle": True,
            "has_preconditions": True,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": True,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Remote Honk & Flash": {
        "requirements": {
            "needs_vehicle": True,
            "has_preconditions": True,
            "reason_for_block": "Not finished",
            "region_locks": ["chn"]
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "My Car Statistics": {
        "requirements": {
            "needs_vehicle": False,
            "has_preconditions": False,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "My Cabin Comfort": {
        "requirements": {
            "needs_vehicle": True,
            "has_preconditions": True,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "My Battery Charge": {
        "requirements": {
            "needs_vehicle": True,
            "has_preconditions": True,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Service Management": {
        "requirements": {
            "needs_vehicle": False,
            "has_preconditions": False,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Activate Heating": {
        "requirements": {
            "needs_vehicle": True,
            "has_preconditions": True,
            "reason_for_block": "",
            "region_locks": ["eur"]
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Roadside Assistance": {
        "requirements": {
            "needs_vehicle": False,
            "has_preconditions": False,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Data Services": {
        "requirements": {
            "needs_vehicle": False,
            "has_preconditions": False,
            "reason_for_block": "Broken",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "My Alerts": {
        "requirements": {
            "needs_vehicle": True,
            "has_preconditions": True,
            "reason_for_block": "Not finished",
            "region_locks": ["nar"]
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Theft Alarm": {
        "requirements": {
            "needs_vehicle": True,
            "has_preconditions": True,
            "reason_for_block": "",
            "region_locks": ["eur"]
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Stolen Vehicle Locator": {
        "requirements": {
            "needs_vehicle": False,
            "has_preconditions": False,
            "reason_for_block": "Not finished",
            "region_locks": ["nar", "chn"]
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Audials": {
        "requirements": {
            "needs_vehicle": False,
            "has_preconditions": False,
            "reason_for_block": "",
            "region_locks": ["eur", "nar"]
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Car Finder": {
        "requirements": {
            "needs_vehicle": True,
            "has_preconditions": False,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Nav Companion": {
        "requirements": {
            "needs_vehicle": True,
            "has_preconditions": True,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Notifications": {
        "requirements": {
            "needs_vehicle": False,
            "has_preconditions": True,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Push Notifications": {
        "requirements": {
            "needs_vehicle": True,
            "has_preconditions": False,
            "reason_for_block": "Broken",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Profile": {
        "requirements": {
            "needs_vehicle": False,
            "has_preconditions": False,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": True,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Localization": {
        "requirements": {
            "needs_vehicle": False,
            "has_preconditions": False,
            "reason_for_block": "Not automatable",
            "region_locks": []
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Privacy Mode": {
        "requirements": {
            "needs_vehicle": True,
            "has_preconditions": True,
            "reason_for_block": "",
            "region_locks": []
        },
        "fields": {
            "name": True, "email": True, "password": True, "pin": True,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Remote Park Assist": {
        "requirements": {
            "needs_vehicle": True,
            "has_preconditions": True,
            "reason_for_block": "Not automatable",
            "region_locks": []
        },
        "fields": {
            "name": True, "email": True, "password": True, "pin": True,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    },

    "Stolen Vehicle Tracking": {
        "requirements": {
            "needs_vehicle": True,
            "has_preconditions": True,
            "reason_for_block": "",
            "region_locks": ["eur"]
        },
        "fields": {
            "name": False, "email": True, "password": True, "pin": False,
            "vin": False, "vehicle": True, "phone": True, "country": True
        }
    }
}
all_services = list(service_requirements.keys())