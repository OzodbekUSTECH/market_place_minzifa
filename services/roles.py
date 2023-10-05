from repositories import Pagination
from schemas.roles import RoleSchema, CreateRoleSchema, UpdateRoleSchema
from database import UnitOfWork
from utils.exceptions import CustomExceptions
from models import Role

class RolesService:
    def __init__(self):
        self.uow = UnitOfWork()

    async def create_role(self, role_data: CreateRoleSchema) -> Role:
        role_dict = role_data.model_dump()
        async with self.uow:  
            role = await self.uow.roles.create(role_dict)
            await self.uow.commit()          
            return role

    async def get_all_roles(self) -> list[Role]:
        async with self.uow:
            return await self.uow.roles.get_all()
    
    async def get_role_by_id(self, role_id: int) -> Role:
        async with self.uow:
            return await self.uow.roles.get_by_id(role_id)
    
    

    async def update_role(self, role_id: int, role_data: UpdateRoleSchema) -> Role:
        role_dict = role_data.model_dump()
        async with self.uow:   
            role = await self.uow.roles.update(role_id, role_dict)
            await self.uow.commit()         
            return role
    
    async def delete_role(self, role_id: int) -> Role:
        async with self.uow:
            try:
                role = await self.uow.roles.delete(role_id)
                await self.uow.commit()     
                return role
            except:
                raise CustomExceptions.forbidden("Cant be deleted cause user has this role already")
    
roles_service = RolesService()