"""
Marzneshin Panel Example
Simple examples for working with Marzneshin API
"""

import asyncio
from opexcore.marzneshin import MarzneshinManager


async def main():
    # Configuration
    HOST = "https://your-marzneshin-panel.com"
    USERNAME = "admin"
    PASSWORD = "admin_password"

    # Step 1: Get authentication token
    print("🔑 Getting admin token...")
    token_response = await MarzneshinManager.admin_token(HOST, USERNAME, PASSWORD)
    token = token_response.access_token
    print(f"✅ Token received: {token[:20]}...")

    # Step 2: Get current admin info
    print("\n👤 Getting current admin info...")
    current_admin = await MarzneshinManager.get_current_admin(HOST, token)
    print(f"✅ Logged in as: {current_admin.username} (sudo: {current_admin.is_sudo})")

    # Step 3: Get list of all admins
    print("\n👥 Getting list of admins...")
    admins_response = await MarzneshinManager.get_admins(HOST, token, page=1, size=10)
    print("✅ Found admins:")
    for item in admins_response:
        print(f"   - {item.username}")

    # Step 4: Get users list
    print("\n📋 Getting users list...")
    users_response = await MarzneshinManager.get_users(HOST, token, page=1, size=5)
    print(f"✅ Showing {len(users_response)} users:")
    for item in users_response:
        status = "🟢 Active" if item.activated else "🔴 Inactive"
        print(f"   - {item.username}: {status}")
    # Step 5: Get services list
    print("\n🔧 Getting services list...")
    services_response = await MarzneshinManager.get_services(
        HOST, token, page=1, size=5
    )
    print(f"✅ Found {len(services_response)} services:")
    for service in services_response:
        print(f"   - {service.name}")
    # Step 6: Get nodes list
    print("\n🌐 Getting nodes list...")
    nodes_response = await MarzneshinManager.get_nodes(HOST, token, page=1, size=10)
    print(f"✅ Found {len(nodes_response)} nodes:")
    for node in nodes_response:
        status = "🟢 Connected" if node.status == "connected" else "🔴 Disconnected"
        print(f"   - {node.name}: {status}")

    # Step 7: Get system statistics
    print("\n📊 Getting system statistics...")
    users_stats = await MarzneshinManager.get_users_stats(HOST, token)
    print("✅ User Statistics:")
    print(f"   - Total: {users_stats.total}")
    print(f"   - Active: {users_stats.active}")

    # Step 8: Get inbounds list
    print("\n📡 Getting inbounds list...")
    inbounds_response = await MarzneshinManager.get_inbounds(
        HOST, token, page=1, size=5
    )
    print(f"✅ Found {len(inbounds_response)} inbounds:")
    for inbound in inbounds_response:
        print(f"   - {inbound.tag}")
    print("\n✨ All operations completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())
