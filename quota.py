"""Per-tenant quota accounting for the prod residency end-to-end probe."""


class Quota:
    def __init__(self, tenants):
        self.tenants = tenants
        self.used = {}

    def consume(self, tenant, units):
        self.used[tenant] = self.used.get(tenant, 0) + units
        return self.used[tenant] <= self.tenants[tenant]

    def remaining(self, tenant):
        # Bug: a tenant that has consumed more than its allowance reports a
        # negative remaining quota instead of zero.
        return self.tenants[tenant] - self.used.get(tenant, 0)
