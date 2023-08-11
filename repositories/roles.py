from repositories.base import BaseRepository


class RolesRepository(BaseRepository):
    
    async def get_permissions_of_role(self, role_id: int):
        role = await self.get_by_id(role_id)
        return [perm.permission for perm in role.role_permissions]

    

        