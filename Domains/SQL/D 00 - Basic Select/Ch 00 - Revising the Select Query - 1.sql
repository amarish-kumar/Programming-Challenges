/**********************************************************************************************
** HackerRank Challenge - Revising the Select Query - 1                                      **
**      SQL / Basic Select                                                                   **
**                                                                                           **
** https://www.hackerrank.com/challenges/revising-the-select-query                           **
**                                                                                           **
** Query all columns for all American cities in CITY with populations larger than 100,000.   **
** The CountryCode for America is USA.                                                       **
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

Select * from city where countryCode = 'USA' and population > 100000;