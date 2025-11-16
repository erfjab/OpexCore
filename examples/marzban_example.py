"""
Marzban Panel Example
Simple examples for working with Marzban API
"""

import asyncio
from opexcore.marzban import MarzbanManager


async def main():
    # Configuration
    HOST = "https://your-marzban-panel.com"
    USERNAME = "admin"
    PASSWORD = "admin_password"

    # Step 1: Get authentication token
    print("🔑 Getting admin token...")
    token_response = await MarzbanManager.admin_token(HOST, USERNAME, PASSWORD)
    token = token_response.access_token
    print(f"✅ Token received: {token[:20]}...")

    # Step 2: Get current admin info
    print("\n👤 Getting current admin info...")
    current_admin = await MarzbanManager.get_current_admin(HOST, token)
    print(f"✅ Logged in as: {current_admin.username} (sudo: {current_admin.is_sudo})")

    # Step 3: Get list of all admins
    print("\n👥 Getting list of admins...")
    admins = await MarzbanManager.get_admins(HOST, token, limit=10)
    print(f"✅ Found {len(admins)} admins:")
    for admin in admins:
        print(f"   - {admin.username} (sudo: {admin.is_sudo})")

    # Step 4: Get users list
    print("\n📋 Getting users list...")
    users_response = await MarzbanManager.get_users(HOST, token, limit=5)
    print(
        f"✅ Total users: {users_response.total}, showing first {len(users_response.users)}:"
    )
    for user in users_response.users:
        status = "🟢 Active" if user.status == "active" else "🔴 Inactive"
        print(f"   - {user.username}: {status}")

    # Step 5: Get system stats
    print("\n📊 Getting system statistics...")
    system_stats = await MarzbanManager.get_system_stats(HOST, token)
    print("✅ System Stats:")
    print(f"   - Total Users: {system_stats.total_user}")
    print(f"   - Active Users: {system_stats.users_active}")

    # Step 6: Get nodes list
    print("\n🌐 Getting nodes list...")
    nodes = await MarzbanManager.get_nodes(HOST, token)
    print(f"✅ Found {len(nodes)} nodes:")
    for node in nodes:
        status = "🟢 Connected" if node.status == "connected" else "🔴 Disconnected"
        print(f"   - {node.name}: {status}")

    # Step 7: Get core stats
    print("\n⚙️ Getting core statistics...")
    core_stats = await MarzbanManager.get_core_stats(HOST, token)
    print("✅ Core Info:")
    print(f"   - Version: {core_stats.version}")
    print(f"   - Started: {core_stats.started}")

    print("\n✨ All operations completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())
