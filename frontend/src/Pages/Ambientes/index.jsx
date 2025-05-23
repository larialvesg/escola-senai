import { FaEdit, FaTrash, FaPlus, FaSearch } from "react-icons/fa";
// import ModalProfessores from "../../components/modals/teacher";
import Header from "../../Components/header/index.jsx";
import React, { useState, useEffect } from "react";
import axios from "axios";
import "./styles.css";

export default function Ambientes() {
  const [dados, setDados] = useState([]);
  const [modalOpen, setModalOpen] = useState(false);
  const [idSearch, setIdSearch] = useState("");
  const [nameSearch, setNameSearch] = useState("");
  const [seta, setSeta] = useState(false);
  const [itemSelecionado, setItemSelecionado] = useState(null);
  const token = localStorage.getItem("token");

  useEffect(() => {
    if (!token) return;
    const fetchData = async () => {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/api/ambientes",
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );
        setDados(response.data);
      } catch (error) {
        console.error("Erro ao buscar dados:", error);
      }
    };
    fetchData();
  }, [modalOpen]);

  // const apagar = async (id) => {
  //     if (window.confirm("Tem certeza?")) {
  //         try {
  //             await axios.delete(`http://127.0.0.1:8000/api/id/${id}`, {
  //                 headers: { Authorization: `Bearer ${token}` },
  //             });
  //             setDados(dados.filter((professor) => professor.id !== id));
  //         } catch (error) {
  //             console.error(error);
  //         }
  //     }
  // };

  // const editar = (professor) => {
  //     setProfessorSelecionado(professor);
  //     setModalOpen(true);
  // };

  const searchAmbienteId = async (idSearch) => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/buscar/${idSearch}/`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setProfessorSelecionado(response.data); // Atualiza o estado da modal com os dados do professor
    } catch (error) {
      console.error("Erro ao buscar professor:", error);
    }
  };

  const searchTeacherName = async (nameTeacher) => {
    console.log(nameSearch);
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/buscar/nomes/?search=${nameTeacher}`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      console.log(response.data[0]);
      setProfessorSelecionado(response.data[0]); // Atualiza o estado da modal com os dados do professor
      console.log("0000: ", professorSelecionado);
    } catch (error) {
      console.error("Erro ao buscar professor:", error);
    }
  };

  return (
    <div className="container-ambiente">
      <Header />
      <section className="section-ambiente">
        <div className="table-ambiente">
          <div className="header">
            <div className="coluna3">ID</div>
            <div className="coluna4">SIG</div>
            <div className="coluna5">Descrição</div>
            <div className="coluna6">SN</div>
            <div className="coluna7">Responsável</div>
            <div className="coluna1">Icones</div>
          </div>
          {dados.map((ambiente) => (
            <div key={ambiente.id} className="lista">
              <div className="coluna3">
                <span className="id">{ambiente.id}</span>
              </div>
              <div className="coluna4">
                <span className="sig">{ambiente.sig}</span>
              </div>
              <div className="coluna5">
                <span className="descricao">{ambiente.descricao}</span>
              </div>
              <div className="coluna6">
                <span className="sn">{ambiente.sn}</span>
              </div>
              <div className="coluna7">
                <span className="responsavel">{ambiente.responsavel}</span>
              </div>
              <div className="coluna1">
                <FaEdit className="edit" onClick={() => editar(ambiente)} />
                <FaTrash
                  className="delete"
                  onClick={() => apagar(ambiente.id)}
                />
              </div>
            </div>
          ))}
        </div>

        {/* <div className="footer_table">
                    <div className="btn1">
                        <FaPlus className="adicionar" onClick={() => { setProfessorSelecionado(null), setModalOpen(true) }} />
                    </div>

                    <div className="pesquisar">
                        <input
                            className="id_search"
                            placeholder="id"
                            value={idSearch}
                            onChange={(e) => { setIdSearch(e.target.value) }}
                        />
                        <input
                            className="nome_search"
                            placeholder="nome do professor"
                            value={nameSearch}
                            onChange={(e) => { setNameSearch(e.target.value) }}
                        />
                    </div>
                    <div className="btn2">
                        <FaSearch className="procurar" onClick={() => {
                            idSearch ? searchAmbienteId(idSearch) : null,
                                nameSearch ? searchTeacherName(nameSearch) : null, setModalOpen(true)
                        }} />
                    </div>
                </div>
                <ModalProfessores
                    isOpen={modalOpen}
                    onClose={() => { setModalOpen(false)}}
                    professorSelecionado={professorSelecionado}
                /> */}
      </section>
    </div>
  );
}
