from repositories.roles import RolesRepository
from repositories.base import Pagination
from fastapi import HTTPException, status
from schemas.roles import RoleSchema, CreateRoleSchema, UpdateRoleSchema

class RolesService:
    def __init__(self, roles_repo: RolesRepository):
        self.roles_repo: RolesRepository = roles_repo

    async def get_all_roles(self, pagination: Pagination) -> list[RoleSchema]:
        return await self.roles_repo.get_all(pagination)
    
    async def get_role_by_id(self, role_id: int) -> RoleSchema:
        return await self.roles_repo.get_by_id(role_id)
    
    async def create_role(self, role_data: CreateRoleSchema) -> RoleSchema:
        return await self.roles_repo.create(role_data.model_dump())

    async def update_role(self, role_id: int, role_data: UpdateRoleSchema) -> RoleSchema:
        role_dict = role_data.model_dump()
        return await self.roles_repo.update(role_id, role_dict)
    
    async def delete_role(self, role_id: int) -> RoleSchema:
        return await self.roles_repo.delete(role_id)
    
    