"""
Guard Panel Example
Simple examples for working with Guard API
"""

import asyncio
from opexcore.guard import GuardManager


async def main():
    # Configuration
    HOST = "https://your-guard-panel.com"
    USERNAME = "admin"
    PASSWORD = "admin_password"

    # Step 1: Get authentication token
    print("🔑 Getting admin token...")
    token_response = await GuardManager.create_token(HOST, USERNAME, PASSWORD)
    token = token_response.access_token
    print(f"✅ Token received: {token[:20]}...")

    # Step 2: Get current admin info
    print("\n👤 Getting current admin info...")
    current_admin = await GuardManager.get_current_admin(HOST, token)
    print(f"✅ Logged in as: {current_admin.username}")
    print(f"   - Enabled: {'🟢 Yes' if current_admin.enabled else '🔴 No'}")

    # Step 3: Get list of all admins
    print("\n👥 Getting list of admins...")
    admins = await GuardManager.get_admins(HOST, token)
    print(f"✅ Found {len(admins)} admins:")
    for admin in admins:
        status = "🟢 Enabled" if admin.enabled else "🔴 Disabled"
        print(f"   - {admin.username}: {status}")

    # Step 4: Get subscriptions list
    print("\n📋 Getting subscriptions list...")
    subscriptions = await GuardManager.get_subscriptions(HOST, token, page=1, size=5)
    print(f"✅ Found {len(subscriptions)} subscriptions:")
    for sub in subscriptions:
        status = "🟢 Active" if sub.is_active else "🔴 Inactive"
        print(f"   - {sub.username}: {status}")

    # Step 5: Get general statistics
    print("\n📊 Getting general statistics...")
    stats = await GuardManager.get_stats(HOST, token)
    print("✅ General Stats:")
    print(f"   - Total Subscriptions: {stats.total_subscriptions}")
    print(f"   - Active Subscriptions: {stats.active_subscriptions}")
    print(f"   - Total Admins: {stats.total_admins}")

    # Step 6: Get nodes list
    print("\n🌐 Getting nodes list...")
    nodes = await GuardManager.get_nodes(HOST, token)
    print(f"✅ Found {len(nodes)} nodes:")
    for node in nodes:
        status = "🟢 Active" if node.enabled else "🔴 InActive"
        print(f"   - {node.remark}: {status}")

    # Step 7: Get services list
    print("\n🔧 Getting services list...")
    services = await GuardManager.get_services(HOST, token)
    print(f"✅ Found {len(services)} services:")
    for service in services:
        print(f"   - {service.remark}")

    # Step 8: Get subscription statistics
    print("\n📈 Getting subscription statistics...")
    sub_stats = await GuardManager.get_subscription_stats(HOST, token)
    print("✅ Subscription Stats:")
    print(f"   - Active: {sub_stats.active}")
    print(f"   - Expired: {sub_stats.expired}")
    print(f"   - Limited: {sub_stats.limited}")

    print("\n✨ All operations completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())
