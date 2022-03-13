import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import { Dropdown } from 'semantic-ui-react';

export interface IAssoSelectorProps {
  onChange(value: string): void;

  value: string;
  fluid: boolean;
  placeholder: string;
}

const UserSelector = ({
  onChange,
  value,
  fluid,
  placeholder,
}: IAssoSelectorProps) => {
  const [loading, setLoading] = useState(true);
  const [userList, setUserList] = useState([]);
  const [user, setUser] = useState(value);
  const assosListUrl = '/api/users/';

  useEffect(() => {
    fetch(assosListUrl)
      .then((response) => {
        if (response.status === 200) {
          response.json().then((validResponse) => {
            const assosTmp: React.SetStateAction<any[]> = [];
            validResponse.forEach((x: { id: string; full_name: string; }) => {
              assosTmp.push({
                key: x.id,
                value: x,
                text: x.full_name,
              });
            });
            setUserList(assosTmp);
            setLoading(false);
          });
        } else {
          setLoading(false);
        }
      });
  }, []);

  const handleChange = (e, v) => {
    setUser(v.value);
    onChange(v.value);
  };

  return (
    <Dropdown
      options={loading ? [] : userList}
      placeholder={placeholder}
      loading={loading}
      value={user}
      onChange={handleChange}
      multiple
      search
      selection
      deburr
      fluid={fluid}
    />
  );
};

UserSelector.propTypes = {
  onChange: PropTypes.func,
  value: PropTypes.string,
  fluid: PropTypes.bool,
  placeholder: PropTypes.string,
};

UserSelector.defaultProps = {
  onChange: () => {
  },
  value: null,
  fluid: false,
  placeholder: 'Choisir un utilisateur',
};

export default UserSelector;
