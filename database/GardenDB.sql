/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     04.05.2019 17:52:45                          */
/*==============================================================*/


/*==============================================================*/
/* Table: rcell                                                 */
/*==============================================================*/
create table rcell (
   cellid               SERIAL               not null,
   userid               INT4                 not null,
   plantid              INT4                 null,
   is_dug_up            BOOL                 not null,
   is_fertilized        BOOL                 not null,
   weed                 BOOL                 not null,
   grass_stage          INT4                 not null,
   dug_up_time          TIMESTAMP                 null,
   fertil_time          TIMESTAMP                 null,
   constraint PK_RCELL primary key (cellid)
);

/*==============================================================*/
/* Table: rfetus                                                */
/*==============================================================*/
create table rfetus (
   fetusid              SERIAL               not null,
   plant_type           INT4                 not null,
   userid               INT4                 not null,
   fetyscount           INT4                 not null,
   constraint PK_RFETUS primary key (fetusid)
);

/*==============================================================*/
/* Table: rplants                                               */
/*==============================================================*/
create table rplants (
   plantid              SERIAL               not null,
   type_id              INT4                 not null,
   userid               INT4                 not null,
   cell                 INT4                 not null,
   stage                INT4                 not null,
   points               INT4                 not null,
   thirst               INT4                 not null,
   bugs                 INT4                 not null,
   create_time          TIMESTAMP                 not null,
   update_time          TIMESTAMP                 not null,
   constraint PK_RPLANTS primary key (plantid)
);

/*==============================================================*/
/* Table: rproduct                                              */
/*==============================================================*/
create table rproduct (
   productid            SERIAL               not null,
   source               INT4                 null,
   type                 VARCHAR(40)          not null,
   constraint PK_RPRODUCT primary key (productid)
);

/*==============================================================*/
/* Table: rseed                                                 */
/*==============================================================*/
create table rseed (
   seedid               SERIAL               not null,
   plant_type           INT4                 not null,
   userid               INT4                 null,
   seedcount            INT4                 not null,
   constraint PK_RSEED primary key (seedid)
);

/*==============================================================*/
/* Table: ruser                                                 */
/*==============================================================*/
create table ruser (
   userid               SERIAL               not null,
   login                VARCHAR(256)         not null,
   password             VARCHAR(40)          not null,
   email                VARCHAR(254)         not null,
   coins            INT4                 not null,
   constraint PK_RUSER primary key (userid)
);

/*==============================================================*/
/* Table: splantstype                                           */
/*==============================================================*/
create table splantstype (
   plantstypeid         SERIAL               not null,
   file                 VARCHAR(256)         not null,
   fetus                VARCHAR(256)         not null,
   max_points           INT4                 not null,
   name                 VARCHAR(256)         not null,
   seed_price           INT4                 not null,
   fetus_price          INT4                 not null,
   fetus_min            INT4                 not null,
   fetus_max            INT4                 not null,
   constraint PK_SPLANTSTYPE primary key (plantstypeid)
);

alter table rcell
   add constraint FK_RCELL_RELATIONS_RPLANTS foreign key (plantid)
      references rplants (plantid)
      on delete restrict on update restrict;

alter table rcell
   add constraint FK_RCELL_RELATIONS_RUSER foreign key (userid)
      references ruser (userid)
      on delete restrict on update restrict;

alter table rfetus
   add constraint FK_RFETUS_RELATIONS_RUSER foreign key (userid)
      references ruser (userid)
      on delete restrict on update restrict;

alter table rfetus
   add constraint FK_RFETUS_RELATIONS_SPLANTST foreign key (plant_type)
      references splantstype (plantstypeid)
      on delete restrict on update restrict;

alter table rplants
   add constraint FK_RPLANTS_RELATIONS_RUSER foreign key (userid)
      references ruser (userid)
      on delete restrict on update restrict;

alter table rplants
   add constraint FK_RPLANTS_RELATIONS_SPLANTST foreign key (type_id)
      references splantstype (plantstypeid)
      on delete restrict on update restrict;

alter table rplants
   add constraint FK_RPLANTS_RELATIONS_RCELL foreign key (cell)
      references rcell (cellid)
      on delete restrict on update restrict;

alter table rproduct
   add constraint FK_RPRODUCT_RELATIONS_SPLANTST foreign key (source)
      references splantstype (plantstypeid)
      on delete restrict on update restrict;

alter table rseed
   add constraint FK_RSEED_RELATIONS_SPLANTST foreign key (plant_type)
      references splantstype (plantstypeid)
      on delete restrict on update restrict;

alter table rseed
   add constraint FK_RSEED_RELATIONS_RUSER foreign key (userid)
      references ruser (userid)
      on delete restrict on update restrict;

