"""
PasarGuard Panel Example
Simple examples for working with PasarGuard API
"""

import asyncio
from opexcore.pasarguard import PasarGuardManager


async def main():
    # Configuration
    HOST = "https://your-pasarguard-panel.com"
    USERNAME = "admin"
    PASSWORD = "admin_password"

    # Step 1: Get authentication token
    print("🔑 Getting admin token...")
    token_response = await PasarGuardManager.admin_token(HOST, USERNAME, PASSWORD)
    token = token_response.access_token
    print(f"✅ Token received: {token[:20]}...")

    # Step 2: Get current admin info
    print("\n👤 Getting current admin info...")
    current_admin = await PasarGuardManager.get_current_admin(HOST, token)
    print(f"✅ Logged in as: {current_admin.username}")
    print(f"   - Telegram ID: {current_admin.telegram_id or 'Not set'}")
    print(f"   - Sudo: {'🟢 Yes' if current_admin.is_sudo else '🔴 No'}")

    # Step 3: Get list of all admins
    print("\n👥 Getting list of admins...")
    admins = await PasarGuardManager.get_admins(HOST, token, limit=10)
    print(f"✅ Found {len(admins)} admins:")
    for admin in admins:
        print(f"   - {admin.username} (sudo: {admin.is_sudo})")

    # Step 4: Get users list
    print("\n📋 Getting users list...")
    users_response = await PasarGuardManager.get_users(HOST, token, limit=5)
    print(
        f"✅ Total users: {users_response.total}, showing {len(users_response.users)}:"
    )
    for user in users_response.users:
        status = "🟢 Active" if user.status == "active" else "🔴 Inactive"
        print(f"   - {user.username}: {status}")

    # Step 5: Get system statistics
    print("\n📊 Getting system statistics...")
    system_stats = await PasarGuardManager.get_system_stats(HOST, token)
    print("✅ System Stats:")
    print(f"   - Total Users: {system_stats.total_user}")

    # Step 6: Get nodes list
    print("\n🌐 Getting nodes list...")
    nodes = await PasarGuardManager.get_nodes(HOST, token, limit=10)
    print(f"✅ Found {len(nodes)} nodes:")
    for node in nodes:
        status = "🟢 Connected" if node.status == "connected" else "🔴 Disconnected"
        print(f"   - {node.name}: {status}")

    # Step 7: Get groups list
    print("\n👥 Getting groups list...")
    groups = await PasarGuardManager.get_groups(HOST, token, limit=5)
    print(f"✅ Found {len(groups)} groups:")
    for group in groups:
        print(f"   - {group.name}")

    # Step 8: Get cores list
    print("\n⚙️ Getting cores list...")
    cores = await PasarGuardManager.get_cores(HOST, token, limit=5)
    print(f"✅ Found {len(cores)} cores:")
    for core in cores:
        print(f"   - {core.name}")

    # Step 9: Get hosts list
    print("\n🏠 Getting hosts list...")
    hosts = await PasarGuardManager.get_hosts(HOST, token, limit=5)
    print(f"✅ Found {len(hosts)} hosts:")
    for host in hosts:
        print(f"   - {host.remark}")

    print("\n✨ All operations completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())
