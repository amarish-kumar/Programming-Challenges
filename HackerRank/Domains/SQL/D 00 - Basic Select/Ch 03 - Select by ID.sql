/**********************************************************************************************
** HackerRank Challenge - Select by ID                                                       **
**      SQL / Basic Select                                                                   **
**                                                                                           **
** https://www.hackerrank.com/challenges/select-by-id                                        **
**                                                                                           **
** Query all columns for a city in CITY with the ID 1661.                                    **
**                                                                                           **
** ====Input Format====                                                                      **
** The CITY table is described as follows:                                                   **
**                                                                                           **
**              CITY                                                                         **
** ================================                                                          **
** | Field        | Type          |                                                          **
** ================================                                                          **
** | ID           | NUMBER        |                                                          **
** --------------------------------                                                          **
** | NAME         | VARCHAR2 (17) |                                                          **
** --------------------------------                                                          **
** | COUNTRYCODE  | VARCHAR2 (3)  |                                                          **
** --------------------------------                                                          **
** | DISTRICT     | VARCHAR2 (20) |                                                          **
** --------------------------------                                                          **
** | Population   | NUMBER        |                                                          **
** --------------------------------                                                          **
**                                                                                           **
**********************************************************************************************/

select * from city where id = 1661;