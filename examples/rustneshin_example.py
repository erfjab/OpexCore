"""
Rustneshin Panel Example
Simple examples for working with Rustneshin API
"""

import asyncio
from datetime import datetime, timedelta
from opexcore.rustneshin import RustneshinManager


async def main():
    # Configuration
    HOST = "https://your-rustneshin-panel.com"
    USERNAME = "admin"
    PASSWORD = "admin_password"

    # Step 1: Get authentication token
    print("🔑 Getting admin token...")
    token_response = await RustneshinManager.admin_token(HOST, USERNAME, PASSWORD)
    token = token_response.access_token
    print(f"✅ Token received: {token[:20]}...")
    print(f"   Is Sudo: {token_response.is_sudo}")

    # Step 2: Get current admin info
    print("\n👤 Getting current admin info...")
    current_admin = await RustneshinManager.get_current_admin(HOST, token)
    print(f"✅ Logged in as: {current_admin.username}")
    print(f"   Is Sudo: {current_admin.is_sudo}")
    print(f"   Enabled: {current_admin.enabled}")

    # Step 3: Get list of all admins
    print("\n👥 Getting list of admins...")
    admins_page = await RustneshinManager.get_admins(HOST, token)
    print(f"✅ Found {admins_page.total} admins:")
    for admin in admins_page.items:
        print(f"   - {admin.username} (sudo: {admin.is_sudo})")

    # Step 4: Get users list
    print("\n📋 Getting users list...")
    users_page = await RustneshinManager.get_users(HOST, token)
    print(f"✅ Total users: {users_page.total}, showing first {len(users_page.items)}:")
    for user in users_page.items:
        status = "🟢 Active" if user.is_active else "🔴 Inactive"
        print(f"   - {user.username}: {status}")

    # Step 5: Get system stats
    print("\n📊 Getting system statistics...")
    users_stats = await RustneshinManager.get_users_stats(HOST, token)
    print("✅ Users Stats:")
    print(f"   - Total Users: {users_stats.total}")
    print(f"   - Active Users: {users_stats.active}")
    print(f"   - Expired Users: {users_stats.expired}")
    print(f"   - Limited Users: {users_stats.limited}")
    print(f"   - Online Users: {users_stats.online}")

    # Step 6: Get nodes stats
    print("\n🌐 Getting nodes stats...")
    nodes_stats = await RustneshinManager.get_nodes_stats(HOST, token)
    print("✅ Nodes Stats:")
    print(f"   - Total: {nodes_stats.total}")
    print(f"   - Healthy: {nodes_stats.healthy}")
    print(f"   - Unhealthy: {nodes_stats.unhealthy}")

    # Step 7: Get nodes list
    print("\n🖥️ Getting nodes list...")
    nodes_page = await RustneshinManager.get_nodes(HOST, token)
    print(f"✅ Found {nodes_page.total} nodes:")
    for node in nodes_page.items:
        status = (
            "🟢 Healthy"
            if node.status.value == "healthy"
            else "🔴 " + node.status.value
        )
        print(f"   - {node.name}: {status}")

    # Step 8: Get services list
    print("\n📦 Getting services list...")
    services_page = await RustneshinManager.get_services(HOST, token)
    print(f"✅ Found {services_page.total} services:")
    for service in services_page.items:
        print(
            f"   - {service.name or f'Service #{service.id}'}: {service.user_count} users"
        )

    # Step 9: Get inbounds list
    print("\n📡 Getting inbounds list...")
    inbounds_page = await RustneshinManager.get_inbounds(HOST, token)
    print(f"✅ Found {inbounds_page.total} inbounds:")
    for inbound in inbounds_page.items:
        print(f"   - {inbound.tag}: {inbound.protocol.value}")

    # Step 10: Get traffic stats
    print("\n📈 Getting traffic statistics...")
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=7)
    traffic_stats = await RustneshinManager.get_traffic_stats(
        HOST, token, start=start_date, end=end_date
    )
    print("✅ Traffic Stats (last 7 days):")
    print(f"   - Total: {traffic_stats.total / (1024**3):.2f} GB")

    # Step 11: Get admin stats
    print("\n👑 Getting admin statistics...")
    admins_stats = await RustneshinManager.get_admins_stats(HOST, token)
    print(f"✅ Total Admins: {admins_stats.total}")

    print("\n✨ All operations completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())
