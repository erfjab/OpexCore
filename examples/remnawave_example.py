"""
Remnawave Panel Example
Simple examples for working with Remnawave API
"""

import asyncio
from datetime import datetime, timedelta
from opexcore.remnawave import (
    RemnawaveManager,
    RemnawaveUserCreate,
)


async def main():
    # Configuration
    HOST = "https://your-remnawave-panel.com"
    USERNAME = "admin"
    PASSWORD = "admin_password"

    # Step 1: Login and get authentication token
    print("🔑 Logging in as admin...")
    token_response = await RemnawaveManager.admin_login(HOST, USERNAME, PASSWORD)
    token = token_response.access_token
    print(f"✅ Token received: {token[:20]}...")

    # Step 2: Get system statistics
    print("\n📊 Getting system statistics...")
    system_stats = await RemnawaveManager.get_system_stats(HOST, token)
    print("✅ System Stats:")
    print(f"   - Active Users: {system_stats.user_stats.active}")
    print(f"   - Disabled Users: {system_stats.user_stats.disabled}")
    print(f"   - Limited Users: {system_stats.user_stats.limited}")
    print(f"   - Expired Users: {system_stats.user_stats.expired}")
    print(f"   - Online Now: {system_stats.online_stats.online_now}")
    print(f"   - Online Nodes: {system_stats.nodes.total_online}")

    # Step 3: Get list of all users
    print("\n👥 Getting users list...")
    users = await RemnawaveManager.get_users(HOST, token, size=5)
    print(f"✅ Found {len(users)} users:")
    for user in users[:5]:
        status_emoji = {
            "ACTIVE": "🟢",
            "DISABLED": "🔴",
            "LIMITED": "🟡",
            "EXPIRED": "⚫",
        }
        emoji = status_emoji.get(user.status, "⚪")
        print(f"   {emoji} {user.username}: {user.status}")

    # Step 4: Create a new user
    print("\n➕ Creating a new user...")
    expire_date = (datetime.now() + timedelta(days=30)).isoformat()
    new_user_data = RemnawaveUserCreate(
        username="test_user_001",
        expire_at=expire_date,
        traffic_limit_bytes=10 * 1024 * 1024 * 1024,  # 10 GB
        description="Test user created via API",
        tag="API",
    )
    try:
        new_user = await RemnawaveManager.create_user(HOST, token, new_user_data)
        print(f"✅ User created: {new_user.username}")
        print(f"   - UUID: {new_user.uuid}")
        print(f"   - Short UUID: {new_user.short_uuid}")
        print(f"   - Subscription URL: {new_user.subscription_url}")
    except Exception as e:
        print(f"⚠️ Could not create user (might already exist): {e}")

    # Step 5: Get list of all nodes
    print("\n🌐 Getting nodes list...")
    nodes = await RemnawaveManager.get_nodes(HOST, token)
    print(f"✅ Found {len(nodes)} nodes:")
    for node in nodes:
        status = "🟢 Online" if node.is_node_online else "🔴 Offline"
        xray_status = "✅ Running" if node.is_xray_running else "❌ Stopped"
        print(f"   - {node.name} ({node.country_code}): {status}, Xray: {xray_status}")
        if node.users_online:
            print(f"     Users online: {node.users_online}")

    # Step 6: Get list of all hosts
    print("\n🏠 Getting hosts list...")
    hosts = await RemnawaveManager.get_hosts(HOST, token)
    print(f"✅ Found {len(hosts)} hosts:")
    for host_item in hosts[:5]:
        status = "🔴 Disabled" if host_item.is_disabled else "🟢 Enabled"
        hidden = "👁️ Hidden" if host_item.is_hidden else "👁️‍🗨️ Visible"
        print(f"   - {host_item.remark}: {status}, {hidden}")
        print(f"     Address: {host_item.address}:{host_item.port}")

    # Step 7: Get subscription info (public endpoint - no auth needed)
    print("\n📋 Getting subscription info...")
    if users:
        try:
            first_user = users[0]
            subscription = await RemnawaveManager.get_subscription_info(
                HOST, first_user.short_uuid
            )
            print(f"✅ Subscription Info for {subscription.username}:")
            print(f"   - Days Left: {subscription.days_left}")
            print(f"   - Traffic Used: {subscription.traffic_used}")
            print(f"   - Traffic Limit: {subscription.traffic_limit}")
            print(f"   - Status: {subscription.user_status}")
            print(f"   - Active: {'Yes' if subscription.is_active else 'No'}")
        except Exception as e:
            print(f"⚠️ Could not get subscription info: {e}")

    # Step 8: User management operations
    if users:
        print("\n🔧 Testing user management operations...")
        test_user = users[0]

        # Disable user
        print(f"   Disabling user {test_user.username}...")
        try:
            disabled_user = await RemnawaveManager.disable_user(
                HOST, token, test_user.uuid
            )
            print(f"   ✅ User disabled: {disabled_user.status}")

            # Enable user again
            print(f"   Enabling user {test_user.username}...")
            enabled_user = await RemnawaveManager.enable_user(
                HOST, token, test_user.uuid
            )
            print(f"   ✅ User enabled: {enabled_user.status}")
        except Exception as e:
            print(f"   ⚠️ Could not perform user operations: {e}")

    print("\n✨ All operations completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())
