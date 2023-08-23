from repositories.base import BaseRepository
from schemas.roles import RoleSchema, CreateRoleSchema, UpdateRoleSchema
from sqlalchemy import func


class RolesRepository(BaseRepository):
    
    async def get_permissions_of_role(self, role_id: int):
        role = await self.get_by_id(role_id)
        return role.permissions

    async def has_already_role_name(self, role_data: CreateRoleSchema) -> bool:
        roles = self.session.query(self.model).all()
        existing_role_names = [r.name.lower() for r in roles]  

        return role_data.name.lower() in existing_role_names
        
        

        