from core.blacklist import load_domains

BLOCKED_DOMAINS = load_domains()


def is_blocked(domain):
    domain = domain.lower()
    domain = domain.rstrip(".")
    parts = domain.split(".")
    for i in range(len(parts)-1):
        condidate = ".".join(parts[i:])
        if condidate in BLOCKED_DOMAINS :
            return True   # Return True if the domain or any parent domain is blacklisted .
    return False

