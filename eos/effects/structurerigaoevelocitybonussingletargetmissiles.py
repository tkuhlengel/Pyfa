# Not used by any item
type = "passive"
def handler(fit, src, context):
    groups = ("Structure Anti-Subcapital Missile", "Structure Anti-Capital Missile")

    fit.modules.filteredItemBoost(lambda mod: mod.charge.group.name in groups,
                                     "aoeVelocity", src.getModifiedItemAttr("structureRigMissileExploVeloBonus"),
                                     stackingPenalties=True)
