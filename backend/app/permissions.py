from __future__ import annotations

from typing import Any


DEFAULT_ACCESS_RULES = [
    {
        "role": "CEO",
        "plantsScope": "All plants",
        "canCreateProjects": False,
        "canUploadDocuments": False,
        "canDownloadDocuments": True,
        "canAccessDashboard": True,
        "canAccessPlants": True,
        "canAccessProjects": True,
        "canAccessDocuments": True,
        "canAccessAnalytics": True,
        "canAccessAuditLogs": True,
        "canAccessSessions": True,
        "canAccessSettings": True,
        "canAccessUsers": True,
        "canAccessMasterData": True,
        "canAccessAccessControl": True,
        "canAccessIpConfiguration": False,
        "canEditDocuments": True,
        "canDeleteDocuments": True,
        "canManageUsers": True,
        "canConfigureIp": False,
    },
    {
        "role": "Mining Manager",
        "plantsScope": "Assigned plant only",
        "canCreateProjects": True,
        "canUploadDocuments": True,
        "canDownloadDocuments": False,
        "canAccessDashboard": True,
        "canAccessPlants": True,
        "canAccessProjects": True,
        "canAccessDocuments": True,
        "canAccessAnalytics": False,
        "canAccessAuditLogs": False,
        "canAccessSessions": False,
        "canAccessSettings": True,
        "canAccessUsers": False,
        "canAccessMasterData": False,
        "canAccessAccessControl": False,
        "canAccessIpConfiguration": False,
        "canEditDocuments": False,
        "canDeleteDocuments": False,
        "canManageUsers": False,
        "canConfigureIp": False,
    },
    {
        "role": "Admin",
        "plantsScope": "Governance view",
        "canCreateProjects": False,
        "canUploadDocuments": False,
        "canDownloadDocuments": True,
        "canAccessDashboard": True,
        "canAccessPlants": True,
        "canAccessProjects": True,
        "canAccessDocuments": True,
        "canAccessAnalytics": True,
        "canAccessAuditLogs": True,
        "canAccessSessions": True,
        "canAccessSettings": True,
        "canAccessUsers": True,
        "canAccessMasterData": True,
        "canAccessAccessControl": True,
        "canAccessIpConfiguration": True,
        "canEditDocuments": True,
        "canDeleteDocuments": True,
        "canManageUsers": True,
        "canConfigureIp": True,
    },
]


def get_access_rules(db) -> list[dict[str, Any]]:
    settings = db.app_settings.find_one({"_id": "access_rules"})
    if settings and isinstance(settings.get("rules"), list):
        return settings["rules"]
    db.app_settings.update_one(
        {"_id": "access_rules"},
        {"$setOnInsert": {"rules": DEFAULT_ACCESS_RULES}},
        upsert=True,
    )
    return DEFAULT_ACCESS_RULES


def save_access_rules(db, rules: list[dict[str, Any]]) -> list[dict[str, Any]]:
    db.app_settings.update_one(
        {"_id": "access_rules"},
        {"$set": {"rules": rules}},
        upsert=True,
    )
    return rules


def get_access_rule_for_role(db, role: str) -> dict[str, Any]:
    fallback = next((rule for rule in DEFAULT_ACCESS_RULES if rule.get("role") == role), None)
    rules = get_access_rules(db)
    for rule in rules:
        if rule.get("role") == role:
            return {**(fallback or {}), **rule}
    if fallback:
        return fallback
    return {"role": role, "plantsScope": "Controlled by administrator"}


def user_capabilities(user: dict[str, Any], db) -> dict[str, bool]:
    rule = get_access_rule_for_role(db, user.get("role", ""))
    capabilities = {
        "canCreateProjects": bool(rule.get("canCreateProjects")),
        "canUploadDocuments": bool(rule.get("canUploadDocuments")),
        "canDownloadDocuments": bool(rule.get("canDownloadDocuments")),
        "canAccessDashboard": bool(rule.get("canAccessDashboard")),
        "canAccessPlants": bool(rule.get("canAccessPlants")),
        "canAccessProjects": bool(rule.get("canAccessProjects")),
        "canAccessDocuments": bool(rule.get("canAccessDocuments")),
        "canAccessAnalytics": bool(rule.get("canAccessAnalytics")),
        "canAccessAuditLogs": bool(rule.get("canAccessAuditLogs")),
        "canAccessSessions": bool(rule.get("canAccessSessions")),
        "canAccessSettings": bool(rule.get("canAccessSettings")),
        "canAccessUsers": bool(rule.get("canAccessUsers")),
        "canAccessMasterData": bool(rule.get("canAccessMasterData")),
        "canAccessAccessControl": bool(rule.get("canAccessAccessControl")),
        "canAccessIpConfiguration": bool(rule.get("canAccessIpConfiguration")),
        "canEditDocuments": bool(rule.get("canEditDocuments")),
        "canDeleteDocuments": bool(rule.get("canDeleteDocuments")),
        "canManageUsers": bool(rule.get("canManageUsers")),
        "canConfigureIp": bool(rule.get("canConfigureIp")),
    }
    overrides = user.get("capability_overrides") if isinstance(user.get("capability_overrides"), dict) else {}
    for key, value in overrides.items():
        if key in capabilities and isinstance(value, bool):
            capabilities[key] = value
    return capabilities


def user_has_capability(user: dict[str, Any], capability: str, db) -> bool:
    return user_capabilities(user, db).get(capability, False)
