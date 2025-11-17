"""
OVPanel Example
Simple examples for working with OVPanel API
"""

import asyncio
from datetime import date, timedelta
from opexcore.ovpanel import (
    OVPanelManager,
    OVPanelCreateUser,
    OVPanelUpdateUser,
    OVPanelNodeCreate,
)


async def main():
    # Configuration
    HOST = "https://your-ovpanel.com"
    USERNAME = "admin"
    PASSWORD = "admin_password"

    # Step 1: Get authentication token
    print("🔑 Logging in to OVPanel...")
    token_response = await OVPanelManager.login(HOST, USERNAME, PASSWORD)
    token = token_response.access_token
    print(f"✅ Token received: {token[:20]}...")

    # Step 2: Get all users
    print("\n👥 Getting all users...")
    users_response = await OVPanelManager.get_all_users(HOST, token)
    if users_response.success:
        print(f"✅ {users_response.msg}")
        if users_response.data:
            print(f"   Found users: {users_response.data}")
    else:
        print(f"❌ {users_response.msg}")

    # Step 3: Create a new user
    print("\n➕ Creating a new user...")
    new_user = OVPanelCreateUser(
        name="testuser",
        expiry_date=date.today() + timedelta(days=30),
    )
    create_response = await OVPanelManager.create_user(HOST, token, new_user)
    if create_response.success:
        print(f"✅ User created: {create_response.msg}")
    else:
        print(f"❌ {create_response.msg}")

    # Step 4: Update user status
    print("\n🔄 Updating user status...")
    update_user = OVPanelUpdateUser(
        name="testuser",
        expiry_date=date.today() + timedelta(days=60),
        status=True,
    )
    update_response = await OVPanelManager.change_user_status(HOST, token, update_user)
    if update_response.success:
        print(f"✅ User updated: {update_response.msg}")
    else:
        print(f"❌ {update_response.msg}")

    # Step 5: Get all nodes
    print("\n🌐 Getting all nodes...")
    nodes_response = await OVPanelManager.list_nodes(HOST, token)
    if nodes_response.success:
        print(f"✅ {nodes_response.msg}")
        if nodes_response.data:
            print(f"   Found nodes: {nodes_response.data}")
    else:
        print(f"❌ {nodes_response.msg}")

    # Step 6: Add a new node
    print("\n➕ Adding a new node...")
    new_node = OVPanelNodeCreate(
        name="testnode",
        address="192.168.1.100",
        port=8080,
        key="your-secret-key-here",
        protocol="tcp",
        ovpn_port=1194,
        status=True,
    )
    node_response = await OVPanelManager.add_node(HOST, token, new_node)
    if node_response.success:
        print(f"✅ Node added: {node_response.msg}")
    else:
        print(f"❌ {node_response.msg}")

    # Step 7: Get node status
    print("\n📊 Getting node status...")
    try:
        status_response = await OVPanelManager.get_node_status(
            HOST, token, "192.168.1.100"
        )
        if status_response.success:
            print(f"✅ Node status: {status_response.msg}")
            if status_response.data:
                print(f"   Status data: {status_response.data}")
        else:
            print(f"❌ {status_response.msg}")
    except Exception as e:
        print(f"❌ Error getting node status: {e}")

    # Step 8: Get panel settings
    print("\n⚙️ Getting panel settings...")
    settings_response = await OVPanelManager.get_settings(HOST, token)
    if settings_response.success:
        print(f"✅ Settings retrieved: {settings_response.msg}")
        if settings_response.data:
            print(f"   Settings: {settings_response.data}")
    else:
        print(f"❌ {settings_response.msg}")

    # Step 9: Get server information
    print("\n💻 Getting server information...")
    server_info = await OVPanelManager.get_server_info(HOST, token)
    if server_info.success:
        print(f"✅ Server info: {server_info.msg}")
        if server_info.data:
            print(f"   Server data: {server_info.data}")
    else:
        print(f"❌ {server_info.msg}")

    # Step 10: Get all admins
    print("\n👑 Getting all admins...")
    admins_response = await OVPanelManager.get_all_admins(HOST, token)
    if admins_response.success:
        print(f"✅ {admins_response.msg}")
        if admins_response.data:
            print(f"   Found admins: {admins_response.data}")
    else:
        print(f"❌ {admins_response.msg}")

    # Step 11: Delete user (cleanup)
    print("\n🗑️ Deleting test user...")
    try:
        await OVPanelManager.delete_user(HOST, token, "testuser")
        print("✅ User deleted successfully")
    except Exception as e:
        print(f"❌ Error deleting user: {e}")

    # Step 12: Delete node (cleanup)
    print("\n🗑️ Deleting test node...")
    try:
        delete_node_response = await OVPanelManager.delete_node(
            HOST, token, "192.168.1.100"
        )
        if delete_node_response.success:
            print(f"✅ Node deleted: {delete_node_response.msg}")
        else:
            print(f"❌ {delete_node_response.msg}")
    except Exception as e:
        print(f"❌ Error deleting node: {e}")

    print("\n✨ All operations completed!")


if __name__ == "__main__":
    asyncio.run(main())
