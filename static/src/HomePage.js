import React from 'react';
import Divider from '@material-ui/core/Divider';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import { makeStyles } from '@material-ui/core/styles';



const useStyles = makeStyles({
    table: {
      minWidth: 650,
    },
    tab:{
        padding: "2%",
    }
  });
  


export default class HomePage extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            content: [
                { 'kind': 'drive#file', 'id': '1dfKwGSJpkyWEHtgWh7BWkvt5wUFrg3TCCkza6QhJPLo', 'name': 'this is for testing  purpose', 'mimeType': 'application/vnd.google-apps.document', 'createdTime': '2020-02-23T04:40:33.504Z', 'modifiedTime': '2020-02-23T04:40:54.895Z' },
                { 'kind': 'drive#file', 'id': '1eLL44ZLi7vJCcPj6ROkirYSjzFXveGi_', 'name': 'hash.java.txt', 'mimeType': 'text/plain', 'createdTime': '2020-02-23T02:13:57.671Z', 'modifiedTime': '2020-02-23T02:13:57.671Z' },
                { 'kind': 'drive#file', 'id': '1ZHKl1xOq3Yweweu3voTXN1Cs8OcT5PDXLE6_uxdqwaA', 'name': 'abc', 'mimeType': 'application/vnd.google-apps.document', 'createdTime': '2020-02-22T19:17:19.660Z', 'modifiedTime': '2020-02-22T21:19:02.312Z' },
                { 'kind': 'drive#file', 'id': '0B-iS8K9sHAktc3RhcnRlcl9maWxl', 'name': 'Getting started', 'mimeType': 'application/pdf', 'createdTime': '2020-02-21T11:19:07.865Z', 'modifiedTime': '2020-02-21T11:19:07.865Z' }
            ]
        }
    }

    render() {
        return (
            <Container>
                <Typography variant="h2">
                    Google Drive
                </Typography>
                <Divider />
                <br/>
                <TableContainer component={Paper} className={useStyles.tab}>
                    <Table className={useStyles.table} aria-label="simple table">
                        <TableBody>
                            {this.state.content.map(row => (
                                <TableRow key={row.name}>
                                    <TableCell component="th" scope="row">
                                        {row.name}
                                    </TableCell>
                                    <TableCell align="right">{row.mimeType}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </TableContainer>
            </Container>
        )
    }
}