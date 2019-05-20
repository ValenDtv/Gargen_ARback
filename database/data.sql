insert into ruser(login, password, email, coins) values ('test', '1', 'test@mail.ru',10);

insert into splantstype(file, fetus, max_points, name, seed_price, fetus_price, fetus_min, fetus_max) values ('Tree','Плод',6000,'Дерево',3,1,2,5);
insert into splantstype(file, fetus, max_points, name, seed_price, fetus_price, fetus_min, fetus_max) values ('AppleWood','Яблоко',7200,'Яблоня',5,2,4,8);

insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,false,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,false,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,false,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,false,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,false,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,false,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,true,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,true,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,true,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,false,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,false,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,true,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,true,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,true,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,false,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,false,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,true,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,true,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,true,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,false,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,false,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,false,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,false,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,false,false,false,0,NULL,NULL);
insert into rcell(userid, plantid, is_dug_up, is_fertilized, weed, grass_stage, dug_up_time, fertil_time) values (1,NULL,false,false,false,0,NULL,NULL);


insert into rplants(type_id, userid, cell, stage, points, thirst, bugs, create_time, update_time) values (1,1,12,1,6000,4,3,'09.02.2019 7:16:55','09.02.2019 14:23:17');
insert into rplants(type_id, userid, cell, stage, points, thirst, bugs, create_time, update_time) values (1,1,14,2,2000,1,2,'25.02.2019 7:16:55','25.02.2019 14:23:17');

update rcell set plantid = 1 where cellid = 12;
update rcell set plantid = 2 where cellid = 14;

insert into rproduct(source, type) values (2,'seed');

insert into rfetus(plant_type, userid, fetyscount) values (2,1,3);
insert into rfetus(plant_type, userid, fetyscount) values (1,1,0);

insert into rseed(plant_type, userid, seedcount) values (1,1,2);
insert into rseed(plant_type, userid, seedcount) values (2,1,0);