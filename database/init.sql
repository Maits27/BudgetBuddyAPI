CREATE TABLE users (
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    profile_image TEXT,
    PRIMARY KEY (email)
);
CREATE TABLE gastos (
    nombre TEXT NOT NULL,
    cantidad REAL NOT NULL,
    fecha INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    location TEXT,
    user_id TEXT NOT NULL,
    id TEXT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (email) ON UPDATE NO ACTION ON DELETE CASCADE 
);

INSERT INTO users VALUES('BudgetBuddy','budgetbuddy46@gmail.com','3c9909afec25354d551dae21590bb26e38d53f2173b8d3dc3eee4c047e7ab1c1eb8b85103e3be7ba613b31bb5c9c36214dc9f14a42fd7a2fdb84856bca5c44c2');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 21',10.0,19783,'Comida','budgetbuddy46@gmail.com','0ec58589-da81-4e14-bbec-49f1efabe88b');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 51',4.0,19803,'Ropa','budgetbuddy46@gmail.com','1a1d62f0-a56b-4de0-923f-3b0bf306019a');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 41',5.0,19793,'Hogar','budgetbuddy46@gmail.com','72ed2504-f608-49da-85fe-f597793b4622');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 61',10.0,19814,'Transporte','budgetbuddy46@gmail.com','25f9b362-33ea-4fe3-8d06-54a11ad80b6c');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 71',4.0,19834,'Comida','budgetbuddy46@gmail.com','a6534cf0-80a2-4b30-8a3d-69a6409b85bc');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 81',5.0,19824,'Actividad','budgetbuddy46@gmail.com','65135807-ed52-425e-8878-28aee4f76cce');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 91',1.0,19813,'Otros','budgetbuddy46@gmail.com','441b01e3-7f9f-4639-9525-f0409bf10304');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 22',20.0,19784,'Comida','budgetbuddy46@gmail.com','447f5f86-c653-481f-b1af-2de5a676a180');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 52',8.0,19804,'Ropa','budgetbuddy46@gmail.com','dadce5c7-ce95-4b60-8a88-6e5df18af154');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 42',10.0,19794,'Hogar','budgetbuddy46@gmail.com','6cd2580f-4e1e-4f94-b265-7045f12fda5b');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 62',20.0,19815,'Transporte','budgetbuddy46@gmail.com','32368f2f-9706-436c-a990-db98bb385fd7');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 72',8.0,19835,'Comida','budgetbuddy46@gmail.com','a06456af-d027-4472-ac79-1cc702910fc4');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 82',10.0,19825,'Actividad','budgetbuddy46@gmail.com','14000de5-da6c-4d95-b55a-1e665078cee7');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 92',2.0,19813,'Otros','budgetbuddy46@gmail.com','e991845b-1b49-47b4-b8e8-c131c65026e8');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 23',30.0,19785,'Comida','budgetbuddy46@gmail.com','15e726d2-3dd1-4872-b10d-2deeb8bc0dcd');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 53',12.0,19805,'Ropa','budgetbuddy46@gmail.com','eddab066-1db0-44e8-aaf3-a3691698e12b');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 43',15.0,19795,'Hogar','budgetbuddy46@gmail.com','c548ce0a-c7ba-4e90-9d54-b861fc4dc43b');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 63',30.0,19816,'Transporte','budgetbuddy46@gmail.com','564e7202-8d52-4896-a164-74982ea1ab7f');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 73',12.0,19836,'Comida','budgetbuddy46@gmail.com','ba9852bf-bfc6-4409-a33d-efcefbd1cbd5');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 83',15.0,19826,'Actividad','budgetbuddy46@gmail.com','4a6b1358-accf-4b5e-a1d4-5e38f8522028');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 93',3.0,19813,'Otros','budgetbuddy46@gmail.com','92b17d21-1f8b-462a-9f0b-8cc2cea584a2');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 24',40.0,19786,'Comida','budgetbuddy46@gmail.com','6690ebcf-4f18-4da7-85d8-f17ac72d8874');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 54',16.0,19806,'Ropa','budgetbuddy46@gmail.com','827cd473-436a-49e4-8302-441cb2c18e93');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 44',20.0,19796,'Hogar','budgetbuddy46@gmail.com','ab396006-4f4f-4066-a400-3aff57599638');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 64',40.0,19817,'Transporte','budgetbuddy46@gmail.com','de3c238c-1733-4e6b-b93f-a3a97437b8d2');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 74',16.0,19837,'Comida','budgetbuddy46@gmail.com','8208db24-5fe7-4e18-bafc-becf50228ddf');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 84',20.0,19827,'Actividad','budgetbuddy46@gmail.com','bec587b7-711d-4daa-bdcc-46d00e702b94');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 94',4.0,19813,'Otros','budgetbuddy46@gmail.com','133db6e9-a2ff-4e52-b83c-ae37025e5a7b');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 25',50.0,19787,'Comida','budgetbuddy46@gmail.com','2ad32466-d371-4f71-9507-8fcaea762f99');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 55',20.0,19807,'Ropa','budgetbuddy46@gmail.com','e92ff5af-14a6-496f-b99b-c25b188df850');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 45',25.0,19797,'Hogar','budgetbuddy46@gmail.com','b5cb64d1-6cff-4c2a-9dda-24d742ea6b50');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 65',50.0,19818,'Transporte','budgetbuddy46@gmail.com','ac8691ce-2ae4-4f54-a190-f09ecc825a00');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 75',20.0,19838,'Comida','budgetbuddy46@gmail.com','b8a16766-210e-4176-81d8-e05c5b36a612');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 85',25.0,19828,'Actividad','budgetbuddy46@gmail.com','2515bb6d-cd5f-4214-ac42-5d1524392320');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 95',5.0,19813,'Otros','budgetbuddy46@gmail.com','6ca7f88c-bb87-4666-af3e-972aa2b38bcc');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 26',60.0,19788,'Comida','budgetbuddy46@gmail.com','81ced323-9157-459c-8189-df1a9a9d0d9d');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 56',24.0,19808,'Ropa','budgetbuddy46@gmail.com','c7c6c8ea-dd5b-44f6-8f20-52ced41ffff6');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 46',30.0,19798,'Hogar','budgetbuddy46@gmail.com','e8ff60df-3694-42da-9782-09f9dfd4bdf9');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 66',60.0,19819,'Transporte','budgetbuddy46@gmail.com','66d78c84-0d86-465f-8b1d-81a2f07734a9');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 76',24.0,19839,'Comida','budgetbuddy46@gmail.com','a541ad2f-088d-4aa1-ad4e-7ad3b72bcfde');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 86',30.0,19829,'Actividad','budgetbuddy46@gmail.com','336b9716-d2e6-4733-90d6-90c08ace3720');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 96',6.0,19813,'Otros','budgetbuddy46@gmail.com','c39e9d5e-271d-475d-acf5-09141b209a21');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 27',70.0,19789,'Comida','budgetbuddy46@gmail.com','6b517136-b707-4b62-812f-20879ea527ea');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 57',28.0,19809,'Ropa','budgetbuddy46@gmail.com','84c02cd6-58ad-4924-88d9-4039b3582f8a');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 47',35.0,19799,'Hogar','budgetbuddy46@gmail.com','32348bf0-046b-4c59-b34e-fa31ffdc2412');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 67',70.0,19820,'Transporte','budgetbuddy46@gmail.com','89774e69-c6c9-4ecc-970d-4c02535d28bf');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 77',28.0,19840,'Comida','budgetbuddy46@gmail.com','85a1d638-65b0-4c4a-a19c-e8e6a1fa9e5e');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 87',35.0,19830,'Actividad','budgetbuddy46@gmail.com','31c073d7-43ec-4413-99c0-d62db8aeaa2a');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 97',7.0,19813,'Otros','budgetbuddy46@gmail.com','b3388fc5-e857-4e80-852a-74eabb088c0d');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 28',80.0,19790,'Comida','budgetbuddy46@gmail.com','118c0f01-5ce4-46ea-a353-8c695163bb6a');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 58',32.0,19810,'Ropa','budgetbuddy46@gmail.com','7907cb01-d3bb-4312-8ef7-295224c71e3f');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 48',40.0,19800,'Hogar','budgetbuddy46@gmail.com','98ffa268-7e71-4f61-a885-93624e0a5af4');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 68',80.0,19821,'Transporte','budgetbuddy46@gmail.com','9762b1c2-5971-4d43-bc11-278f8b865e55');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 78',32.0,19841,'Comida','budgetbuddy46@gmail.com','eab66529-e826-4350-b81f-3bfb871b98e2');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 88',40.0,19831,'Actividad','budgetbuddy46@gmail.com','adb8a8b3-4bb8-4257-9fc3-29ced084ae69');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 98',8.0,19813,'Otros','budgetbuddy46@gmail.com','18d9a2b6-59d6-477b-a10e-260cdb3f678a');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 29',90.0,19791,'Comida','budgetbuddy46@gmail.com','513c8d6d-f400-480f-9728-8b35716cbf47');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 59',36.0,19811,'Ropa','budgetbuddy46@gmail.com','f16274ce-456b-493d-ba0d-26aa906897fd');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 49',45.0,19801,'Hogar','budgetbuddy46@gmail.com','df30e47e-c83c-468d-a883-dfb71ce2a83d');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 69',90.0,19822,'Transporte','budgetbuddy46@gmail.com','c1d66049-b4a7-47b5-ab43-2ef8adea45f4');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 79',36.0,19842,'Comida','budgetbuddy46@gmail.com','3dce78b1-87ef-400a-acb7-add0802d59b1');
INSERT INTO gastos (nombre, cantidad, fecha, tipo, user_id, id) VALUES('Gasto Inicial 89',45.0,19832,'Actividad','budgetbuddy46@gmail.com','ba1beb43-8e49-45a9-a830-0335660fa30a');

